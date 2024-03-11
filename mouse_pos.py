import pyautogui

# Get the current mouse cursor position
while True:
    x, y = pyautogui.position()
    print(f"The mouse cursor is at ({x}, {y})")
