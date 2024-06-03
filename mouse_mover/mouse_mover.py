import pyautogui
import time

def move_mouse():
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y + 10)
        time.sleep(1)
        pyautogui.moveTo(x - 10, y - 10)
        time.sleep(1)

if __name__ == "__main__":
    move_mouse()
