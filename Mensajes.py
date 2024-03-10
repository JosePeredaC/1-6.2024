import pyautogui as pg
import pyautogui
import pyperclip as pyc
import time


frase = str(input("Elige el mensaje que quieres enviar: "))
mensajes= int(input("Numero de mensajes: "))
intervalo=float(input("Introduce el intervalo: "))
pyautogui.PAUSE = intervalo
time.sleep(3)

for i in range(mensajes):
    residuo=mensajes % 10
    pyc.copy(frase)
    pg.hotkey('ctrl','v')
    if residuo == 0:
        time.sleep(15)
    mensajes= mensajes - 1
    pg.press('enter')

