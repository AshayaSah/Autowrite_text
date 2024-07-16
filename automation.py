import pyautogui
import time 
time.sleep(3)
for i in range(10):
    pyautogui.typewrite("Hello World")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)