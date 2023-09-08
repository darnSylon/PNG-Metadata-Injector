from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import subprocess

# Custom event handler class to monitor directory changes
class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()

    # Method to run the observer
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Observer stopped")
        self.observer.join()

# Event handler to execute actions when a file change is detected
class Handler(FileSystemEventHandler):
    @staticmethod
    def process(event):
        # Only proceed for new files
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"Received created event - {event.src_path}.")
            check_and_run_script()

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

def check_and_run_script():
    folder_path = "IN_ADD-Chunk-2-PS"  # The folder to watch
    files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

    # Check for pairs
    for file in files:
        original_file = file
        ps_file = file.replace('.png', '_PS.png')
        
        if original_file in files and ps_file in files:
            print(f"Found a pair: {original_file} and {ps_file}. Running script.")
            subprocess.run(["python", "Part_02_Comfy-2-PS.py"])
            return

if __name__ == "__main__":
    folder_path = "IN_ADD-Chunk-2-PS"  # The folder to watch
    w = Watcher(folder_path)
    w.run()
