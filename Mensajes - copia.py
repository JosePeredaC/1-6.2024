import pyautogui as pg
import pyautogui
import pyperclip as pyc
import time

pyautogui.PAUSE = 0.01
frase = str(input("Elige el mensaje que quieres enviar: "))
mensajes= int(input("Numero de mensajes: "))
time.sleep(3)
pyc.copy(frase)
for i in range(mensajes):   
    pg.hotkey('ctrl','v')
    pg.press('enter')


