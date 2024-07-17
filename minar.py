import pyautogui 
import time
time.sleep(3)

for i in range(1,1000000):
    pyautogui.mouseDown()
    time.sleep(240)
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("w")
    pyautogui.press("w")
   