from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import time
import os

# Set the current working directory to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Assuming the script is in the same directory as the minecraftInstance.json file
source_path = os.path.join(script_directory, "minecraftinstance.json")
destination_path = os.path.join(script_directory, "instance", "instance.json")

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == source_path:
            print(f"{source_path} has been modified.")
            self.update_instance_json()

    def update_instance_json(self):
        try:
            shutil.copyfile(source_path, destination_path)
            print(f"Updated {destination_path} with the latest content from {source_path}.")
        except Exception as e:
            print(f"Error occurred while updating instance.json: {e}")

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=script_directory, recursive=False)

    try:
        observer.start()
        print(f"Watching for changes in {source_path}...")

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
