import pystray
from PIL import Image
import threading
from assistant.SpeechRecognition import listen, stopListen, continueListen

tray_icon = None
jarvis_thread = None

def on_start(icon, item):
    global jarvis_thread

    if jarvis_thread is not None:
        continueListen()

    new_image = Image.open("assistant\\icons\\jarvis_image_active.png")
    icon.icon = new_image
    
    jarvis_thread = threading.Thread(target=listen, daemon=True)
    jarvis_thread.start()

def on_stop(icon, item):
    global jarvis_thread

    stopListen()

    new_image = Image.open("assistant\\icons\\jarvis_image.png")
    icon.icon = new_image
    jarvis_thread.join()

def on_quit(icon, item):
    icon.stop()

def setup_tray_icon():
    global tray_icon
    # Load the initial image for the tray icon
    image = Image.open("assistant\\icons\\jarvis_image.png")
    tray_icon = pystray.Icon('Jarvis', image, menu=pystray.Menu(
        pystray.MenuItem('Start', on_start),
        pystray.MenuItem('Stop', on_stop),
        pystray.MenuItem('Quit', on_quit)
    ))

    tray_icon.run()

def run_tray_icon():
    setup_tray_icon()
