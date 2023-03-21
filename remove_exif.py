# This script will strip all EXIF data jpg/jpeg files from the Desktop/export folder.
# To use, replace folder_path with your own export folder.
# If you get a permission error, enter **chmod +x remove_exif.py** in the terminal to change permissions.
# You will also need to install **piexif**.

import os
import piexif

folder_path = "/users/username/Desktop/export"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        filepath = os.path.join(folder_path, filename)
        try:
            exif_dict = piexif.load(filepath)
            exif_dict.clear()
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, filepath)
            print(f"EXIF data removed from {filename}")
        except:
            print(f"Failed to remove EXIF data from {filename}")
