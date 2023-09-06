import os # OS related functions
import shutil # File operations such as copying
import time
from watchdog.observers import Observer # Observer class to monitor file system events
from watchdog.events import FileSystemEventHandler # Handle file system events 

source_folder = "C:\\Users\\Fatihi\\Desktop\\2"
destination_folder = "C:\\Users\\Fatihi\\Desktop\\3"

class MyHandler(FileSystemEventHandler): # Event handler that inherits from FileSystemEventHandler
    def on_modified(self, event):
        if event.is_directory: # Check if the event is related to a directory
            return
        source_path = event.src_path # Get source path of the modified file
        # Generate desination path by joining destination folder with the relative path from source_folder
        destination_path = os.path.join(destination_folder, os.path.relpath(source_path, source_folder)) 

        os.makedirs(os.path.dirname(destination_path), exist_ok=True) # Ensure the destination folder exists

        shutil.copy2(source_path, destination_path) # Copy or update the file in the destination folder
        print(f"File updated: {source_path} -> {destination_path}")

if __name__ == "__main__":
    event_handler = MyHandler() # Initialize the custom event handler
    observer = Observer() # initialize the observer fro monitoring file system events
    observer.schedule(event_handler, source_folder, recursive=True) # Schedule the event handler to watch the source folder recursively
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
