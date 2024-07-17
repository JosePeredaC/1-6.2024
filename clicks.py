import pyautogui 
import time
clicks = int(input("Numero de clicks: "))
intervalo = float(input("Intervalo en seg: "))
time.sleep(3)

pyautogui.PAUSE = intervalo

for _ in range(clicks):
    pyautogui.click()