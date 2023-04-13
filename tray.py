import pystray
from PIL import Image
import os
import sys

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def on_show_settings():
    # TODO: Open settings dialog
    pass

def on_tray_icon_clicked(icon):
    icon.visible = not icon.visible

def create_tray_icon():
    pathImage = resource_path("./images/icon.png")
    image = Image.open(pathImage)
    menu_items = [
        # pystray.MenuItem('Settings', on_show_settings),
        pystray.MenuItem('Quit', on_quit)
    ]
    menu = pystray.Menu(*menu_items)
    icon = pystray.Icon('Screenshoter', image, 'Screenshoter', menu)
    icon.run()


