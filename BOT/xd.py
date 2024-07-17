from selenium import webdriver
from bs4 import BeautifulSoup
import os
import re
import time


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
os.system("PAUSE")

def leer_mensajes():
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    elementos = soup.find_all(class_="_ao3e selectable-text copyable-text")

    for elemento in elementos:
        texto = elemento.text
        print("Mensaje recibido:", texto)
        
        if re.search(r'-23200[0-3][0-9][0-9]', texto):
            try:
                print("Se encontró el patrón 1 en el mensaje:", texto)
                ruta_imagen = re.search(r'23200[0-3][0-9][0-9]',texto)
                realruta= ruta_imagen.group()
                print(realruta)
                time.sleep(5)
                campo_archivos = driver.find_element("p.selectable-text.copyable-text.x15bjb6t.x1n2onr6")
                campo_archivos.send_keys(ruta_imagen)
            except Exception as e:
                print(f"Error {e}")
        else:
           print("Sigo buscando")

while True:
    leer_mensajes()
    time.sleep(5)  