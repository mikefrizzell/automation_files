import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the path to the downloads directory
downloads_path = '/Users/<username>/Downloads'

# Define a handler for file system events
class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        # When a new file is created, run the unzip script
        os.system('python /path/to/auto_unzip.py')

# Create an observer for the downloads directory
observer = Observer()
observer.schedule(DownloadHandler(), downloads_path)

# Start the observer
observer.start()

try:
    # Keep the observer running indefinitely
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
