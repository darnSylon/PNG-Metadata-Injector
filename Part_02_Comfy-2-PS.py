import os
import shutil

# Function to read PNG chunks from a file
def read_chunks(file_path):
    chunks = []
    with open(file_path, 'rb') as f:
        # Skip PNG header
        f.read(8)
        while True:
            length_bytes = f.read(4)
            if len(length_bytes) == 0:
                break
            length = int.from_bytes(length_bytes, byteorder='big')
            chunk_type = f.read(4)
            chunk_data = f.read(length)
            crc = f.read(4)
            chunks.append((chunk_type, length, chunk_data, crc))
    return chunks

# Function to write PNG chunks to a file
def write_chunks(file_path, chunks):
    with open(file_path, 'wb') as f:
        # Write PNG header
        f.write(b'\x89PNG\r\n\x1a\n')
        for chunk_type, length, chunk_data, crc in chunks:
            f.write(length.to_bytes(4, byteorder='big'))
            f.write(chunk_type)
            f.write(chunk_data)
            f.write(crc)

input_folder = "IN_ADD-Chunk-2-PS"
output_folder = "OUT_FIXED_PS"

for filename in os.listdir(input_folder):
    if filename.endswith("_PS.png"):
        original_filename = filename.replace("_PS.png", ".png")
        copy_filename = filename.replace(".png", "_X.png")
        
        # Extract chunks from the original file
        original_chunks = read_chunks(os.path.join(input_folder, original_filename))
        
        # Extract chunks from the Photoshop file
        ps_chunks = read_chunks(os.path.join(input_folder, filename))
        
        # Create a copy of the Photoshop file with "_X" appended to the filename
        shutil.copy(os.path.join(input_folder, filename), os.path.join(input_folder, copy_filename))
        
        # Inject the metadata chunks into the copied Photoshop file
        new_chunks = []
        for chunk_type, _, chunk_data, crc in ps_chunks:
            if chunk_type == b'IEND':
                for original_chunk_type, original_length, original_chunk_data, original_crc in original_chunks:
                    if original_chunk_type == b'tEXt':
                        new_chunks.append((original_chunk_type, original_length, original_chunk_data, original_crc))
            new_chunks.append((chunk_type, _, chunk_data, crc))
        
        # Write the new chunks to the copied file
        write_chunks(os.path.join(input_folder, copy_filename), new_chunks)
        
        # Move all files to the output folder
        for file_to_move in [original_filename, filename, copy_filename]:
            shutil.move(os.path.join(input_folder, file_to_move), os.path.join(output_folder, file_to_move))
