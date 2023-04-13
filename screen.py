import tkinter as tk
from PIL import ImageGrab, Image
import win32clipboard
import io
import pytesseract
from ocr import detection_text

def copy_image_to_clipboard(img):
    output = io.BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def select_area():
    root = tk.Tk()
    root.attributes('-alpha', 0.3)
    root.configure(bg='black')
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.overrideredirect(True)

    # Создаем Canvas для рисования
    canvas = tk.Canvas(root, bg='black', highlightthickness=0)
    canvas.pack(fill='both', expand=True)

    # Обработчики событий мыши
    def on_mouse_down(event):
        global x1, y1
        x1, y1 = event.x, event.y

    def on_mouse_move(event):
        global x2, y2
        x2, y2 = event.x, event.y
        # Очищаем Canvas и рисуем рамку
        canvas.delete('rectangle')
        canvas.create_rectangle(x1, y1, x2, y2, outline='white', tags='rectangle')

    def on_mouse_up(event):
        global x1, y1, x2, y2
        bbox = (min(x1, x2) + canvas.winfo_x(), min(y1, y2) + canvas.winfo_y(), max(x1, x2) + canvas.winfo_x(), max(y1, y2) + canvas.winfo_y())
        root.destroy()
        img = ImageGrab.grab(bbox)
        img.save('screenshot.png')
        copy_image_to_clipboard(img)
        detection_text('screenshot.png')



    # Привязываем обработчики событий мыши
    canvas.bind('<ButtonPress-1>', on_mouse_down)
    canvas.bind('<B1-Motion>', on_mouse_move)
    canvas.bind('<ButtonRelease-1>', on_mouse_up)

    root.mainloop()

