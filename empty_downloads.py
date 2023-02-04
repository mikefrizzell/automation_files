# This is a simple Python script for MacOS to delete all ZIP, APP, MS Office, and image files from my download folder.
# WARNING: This will delete everything permanently, so make sure you've moved anything you need before running.
# To use: replace <username> with your username and run the script. You can also schedule it with a cron job or using Lingon.

import os
import shutil

downloads_folder = "/Users/<username>/Downloads"

for root, dirs, files in os.walk(downloads_folder):
    for filename in files + dirs:
        file_path = os.path.join(root, filename)
        if filename.endswith(".zip") or filename.endswith(".app") or filename.endswith(".doc") or filename.endswith(".docx") or filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".gif"):
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))
