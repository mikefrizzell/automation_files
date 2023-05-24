import os
import time
from PIL import Image
import pyperclip

# Specify the folder where you want to save the screenshots
save_folder = "path/to/save/folder"

def save_screenshot_from_clipboard():
    # Get the clipboard contents
    clipboard_data = pyperclip.paste()

    # Check if the clipboard data is an image
    if clipboard_data.startswith("data:image"):
        # Create a new PIL Image object from the clipboard data
        image = Image.open(clipboard_data)

        # Generate a unique filename for the image
        filename = f"screenshot_{int(time.time())}.png"  # Use timestamp in the filename

        # Save the image to the specified folder
        image.save(os.path.join(save_folder, filename))
        print("Screenshot saved successfully.")

while True:
    save_screenshot_from_clipboard()
    time.sleep(60)  # Delay between each check (60 seconds in this example)
