from PIL import Image
import pytesseract
import cv2
import os

# Получаем абсолютный путь к исполняемому файлу Tesseract OCR
tesseract_path = os.path.join(os.getcwd(), 'env', 'Scripts', 'pytesseract.exe')

# Указываем путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = tesseract_path


def detection_text_ocr(): 
    
    filename = 'screenshot.png'
    # загрузить образ и преобразовать его в оттенки серого
    #image = cv2.imread(filename)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #gray = cv2.medianBlur(gray, 3)
    
    #cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    #os.remove(filename)
    print(text)


detection_text_ocr()