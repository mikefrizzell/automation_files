# This is a simple Python script to move all PDFs in my Downloads folder to a Books folder in MacOS.
# I download quite a few PDF and EPUB books and this makes it easier to get them into one place.
# WARNING: this will move all PDFs, so if you have a restaurant menu in your downloads, it'll move that as well.
# To use: replace <username> with your username and run the script. You can also schedule it with a cron job or use Lingon to automate.


import os
import shutil

downloads_folder = "/Users/<username>/Downloads"
destination = "/Users/<username>/Documents/Books"

if not os.path.exists(destination):
    os.makedirs(destination)

for filename in os.listdir(downloads_folder):
    if filename.endswith(".pdf") or filename.endswith(".epub"):
        source = os.path.join(downloads_folder, filename)
        dest = os.path.join(destination, filename)
        try:
            shutil.move(source, dest)
        except Exception as e:
            print("Failed to move %s to %s. Reason: %s" % (source, dest, e))
