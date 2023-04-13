import subprocess

def detection_text():
    cmd = ['env\\Scripts\\pytesseract.exe', 'screenshot.png', '-l', 'eng']
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

detection_text()