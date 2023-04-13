# This script just copies certain files from one location to another. I created this because I accidentally deleted an important file at work and had no way to get it back.

import shutil
import os

# List of source folders to backup
source_folders = ["P:\source_folder_1", "P:\source_folder_2", "P:\source_folder_3"]

# Folder for backup
backup_folder = "C:\Users\username\Documents\Backup"

# Loop through each source folder in the list
for source_folder in source_folders:
    # Extract the folder name from the source folder path
    folder_name = os.path.basename(source_folder)
    # Construct destination folder path
    backup_folder_path = os.path.join(backup_folder, folder_name)
    # Check if the backup folder already exists, if not create it
    if not os.path.exists(backup_folder_path):
        os.mkdir(backup_folder_path)
    # Loop through all files and folders in the source folder
    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        backup_item = os.path.join(backup_folder_path, item)
        # Check if the item is a file
        if os.path.isfile(source_item):
            # Check if the source file is newer than the backup file
            if os.path.exists(backup_item) and os.path.getmtime(source_item) <= os.path.getmtime(backup_item):
                print(f"Skipping '{item}' - No changes detected.")
            else:
                # Copy the file to the backup folder
                shutil.copy(source_item, backup_item)
                print(f"Backup created: {backup_item}")
                # Check if the item is a folder
        elif os.path.isdir(source_item):
            # Recursively copy the folder and its contents to the backup folder
            shutil.copytree(source_item, backup_item, dirs_exist_ok=True)
            print(f"Backup created: {backup_item}")
