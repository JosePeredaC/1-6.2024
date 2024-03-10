import pyautogui 
import time
clicks = int(input("Numero de clicks: "))
intervalo = int(input("Intervalo en seg: "))
time.sleep(3)

# Ajusta la velocidad de clics
pyautogui.PAUSE = intervalo

for _ in range(clicks):
    pyautogui.click()