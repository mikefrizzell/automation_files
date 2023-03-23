# This script will run all of the automation scripts you want one after another.
import subprocess

# List of scripts to run
scripts = ['move_pdfs.py', 'empty_downloads.py']

# Loop through the list and run each script
for script in scripts:
    subprocess.run(['python', script])
