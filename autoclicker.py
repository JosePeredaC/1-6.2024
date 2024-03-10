import pyautogui 
import pyperclip as pyc
import time


click= int(input("Numero de click: "))
time.sleep(3)

for i in range(click):
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()