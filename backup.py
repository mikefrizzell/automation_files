# This script just copies certain files from one location to another. I created this because I accidentally deleted an important file at work and had no way to get it back.

import shutil
import os

# List of files to backup
files_to_backup = ["file1.txt", "file2.txt", "file3.txt"]

# Folder for backup
backup_folder = "Backup DO NOT DELETE"

# Create the backup folder if it doesn't exist
if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

# Loop through each file and create a backup
for file in files_to_backup:
    # Construct the source and destination file paths
    src_file = file
    dest_file = os.path.join(backup_folder, file)

    # Copy the file to the backup folder
    shutil.copy(src_file, dest_file)

    print(f"File '{file}' backed up to '{dest_file}'")
