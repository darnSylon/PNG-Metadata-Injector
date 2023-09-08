
# PNG Metadata Injector

## Description
This project consists of two Python scripts that work together to inject metadata from an original PNG image into an altered Photoshop image. The workflow is designed to preserve PNG chunks, which are often lost when an image is edited using software like Adobe Photoshop.

## Scripts
1. `Part_01_Watch_IN.py`: Watches a specified directory for any file changes and triggers the second script when an event occurs.
2. `Part_02_Comfy-2-PS.py`: Reads PNG chunks from the original image and injects them into the altered image.

## Prerequisites
- Python 3.x
- `watchdog` library for Python

## Usage
1. Set the path of the directory you want to watch in `Part_01_Watch_IN.py`.
2. Replace file paths for the original, altered, and output PNGs in `Part_02_Comfy-2-PS.py`.
3. Run `Part_01_Watch_IN.py` to start monitoring the directory.
4. Add or modify files in the watched directory to trigger `Part_02_Comfy-2-PS.py`.

## Current settings
1. Folder structure
Comfy_PNG_PS>
            IN_ADD-Chunk-2-PS
            OUT_FIXED_PS
            Part_01_Watch_IN.py
            Part_02_Comfy-2-PS.py
            LICENSE
            README.md
2. In Comfy_PNG_PS run Python script Part_01_Watch_IN.py.
3. Drop your two files into the 'IN_ADD-Chunk-2-PS' folder. (Example: ComfyUI file: original.png, Photoshop file: original_PS.png)
4. The Part 02 script will trigger and all three files will be in the 'OUT_FIXED_PS' folder. (Original, Photoshop, and new Phototshop with metadata injected.)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
