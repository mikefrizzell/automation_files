# About
 These are a few Python scripts I've written to automate things on my Mac.

# Usage
To use, replace <username> with your own user name. If you want to automate the whole process, schedule the script as a [cron job](https://www.howtogeek.com/devops/what-is-a-cron-job-and-how-do-you-use-them/) or schedule with [Lingon](https://www.peterborgapps.com/lingon/).

# Scripts
* auto_unzip.py - Automatically unzips any .ZIP files in the specified directory (in this case Downloads) and delete the .ZIP file itself. Use this in conjuction with watchdog_scripts/monitor_downloads.py to have this run automatically.
* automate.py - Runs all of your scripts, or the ones you choose to include, all at once. This is useful if you'd rather than run your scripts manually than automating them.
* doc_to_md.py - Converts .DOC and .DOCX files to .MD plaintext files. To run, navigate to the folder and type "python doc_to_md.py input.docx output.md".
* empty_downloads.py - Deletes any files (of the file types listed in the script) in your Downloads folder.
* pdf_to_csv.py - Converts tables in a PDF into a CSV file. This one is still a work in progress and only really works when the entire PDF is a table and there isn't any extraneous information.
* remove_exif.py - Strips EXIF data from image files. This is useful if you'd rather not have any personally identifiable information in the images you share online. NOTE: This removes all EXIF data, including camera, lens, aperture, and shutter speed.
* backup.py - Creates a copy of listed files. This is not a replacement for a full-fledge backup system, just another option for mission critical files.

# License
All scripts are under the MIT License.
