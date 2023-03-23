# This script will automatically unzip all files and delete the archive.
# Use this in conjuction with watchdog_scripts/monitor_downloads.py to completely automate the process.
import os
import zipfile

# Set the path to the downloads directory
downloads_path = '/Users/<username>/Downloads'

# Loop through all files in the downloads directory
for filename in os.listdir(downloads_path):
    filepath = os.path.join(downloads_path, filename)
    # Check if the file is a zip file
    if filename.endswith('.zip'):
        # Extract the contents of the zip file to the same directory
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(downloads_path)
        # Delete the original zip file
        os.remove(filepath)
