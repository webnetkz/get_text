import keyboard
from screen import select_area
from tray import create_tray_icon
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def on_printscreen():
    select_area()


keyboard.add_hotkey('print screen', on_printscreen)
# Здесь можно добавить любой код, который будет выполняться в фоновом режиме
# пока не произойдет нажатие на клавишу PrintScreen
create_tray_icon()
while True:
    pass
