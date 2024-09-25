from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import instance_watcher  # Import the instance_watcher module
import mods_watcher       # Import the mods_watcher module

# Set the current working directory to the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Define paths for the input and output files
source_path = os.path.join(script_directory, "minecraftinstance.json")
destination_path = os.path.join(script_directory, "instance", "instance.json")
mods_destination_path = os.path.join(script_directory, "instance", "mods.json")  # New destination for mods

# FileSystemEventHandler subclass for handling file changes
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == source_path:
            print(f"{source_path} has been modified.")
            # Extract instance information
            instance_watcher.extract_instance_info(source_path, destination_path)
            # Extract mod information
            mods_watcher.extract_mod_info(source_path, mods_destination_path)

if __name__ == "__main__":
    # Create an event handler
    event_handler = FileChangeHandler()

    # Set up the observer
    observer = Observer()
    observer.schedule(event_handler, path=script_directory, recursive=False)

    try:
        observer.start()
        print(f"Watching for changes in {source_path}...")

        while True:
            time.sleep(1)  # Keep the script running

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
