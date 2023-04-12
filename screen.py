import pyautogui

def screenshot_and_copy_to_clipboard():
    # Задержка перед началом выполнения функции, чтобы пользователю дать время убрать все лишние окна
    # и подготовиться к выделению области
    pyautogui.sleep(5)

    # Затемнение экрана
    pyautogui.press('winleft')
    pyautogui.typewrite('color')
    pyautogui.press('enter')
    pyautogui.typewrite('0')
    pyautogui.press('enter')

    # Выделение области
    screenshot_region = pyautogui.screenshot(region=None)

    # Копирование изображения в буфер обмена
    screenshot_region.save("screenshot.png")
    pyautogui.hotkey('ctrl', 'c')

    # Очистка экрана
    pyautogui.press('winleft')
    pyautogui.typewrite('color')
    pyautogui.press('enter')
    pyautogui.typewrite('f')
    pyautogui.press('enter')
