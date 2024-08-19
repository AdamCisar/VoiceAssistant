import pystray
from PIL import Image, ImageDraw
import sys
import threading
import time

# Global variable to control the running state
running = False

# Function to create an image for the icon
def create_image():
    # Create an image with white background
    image = Image.new('RGB', (64, 64), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw a simple icon (a blue square)
    draw.rectangle([(16, 16), (48, 48)], fill=(0, 0, 255))
    
    return image

# Function to handle the "Start" action
def on_start(icon, item):
    global running
    if not running:
        running = True
        print("Started")
        # Simulate a long-running process
        threading.Thread(target=long_running_process).start()

# Function to handle the "Stop" action
def on_stop(icon, item):
    global running
    if running:
        running = False
        print("Stopped")

# Function to simulate a long-running process
def long_running_process():
    while running:
        print("Running...")
        time.sleep(1)

# Function to handle the quit action
def on_quit(icon, item):
    global running
    if running:
        running = False
    icon.stop()
    sys.exit()

# Create the system tray icon
def setup_tray_icon():
    icon = pystray.Icon('test_icon', create_image(), menu=pystray.Menu(
        pystray.MenuItem('Start', on_start),
        pystray.MenuItem('Stop', on_stop),
        pystray.MenuItem('Quit', on_quit)
    ))
    
    # Run the icon in the system tray
    icon.run()

if __name__ == "__main__":
    setup_tray_icon()
