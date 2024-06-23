import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        # print(f"{event.src_path} has been modified. Running the script...")
        print(f"{event.src_path}")
        subprocess.run(["python", event.src_path])


if __name__ == "__main__":
    w = Watcher()
    w.run()
