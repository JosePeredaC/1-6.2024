#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
import time
import tkinter as tk
def guardar_texto_en_txt(texto, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)
def comparar_htmls(aHtml,nHtml):
    with open(aHtml, 'r', encoding='utf-8') as archivo:
        contenido_archivo= archivo.read()
        if contenido_archivo == nHtml:
            return True
        else:
            return False
def mostrar_ventana_emergente(mensaje):
    ventana = tk.Tk()
    ventana.title("Alerta de Cambio en la Página")
    label = tk.Label(ventana, text=mensaje)
    label.pack(padx=20, pady=20)
    ventana.mainloop()
def main(): 
    url= str(input("Ingrese el link de la pagina a analizar: "))
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        texto_a_guardar = html
        nombre_archivo = "htmlanterior.txt"
        guardar_texto_en_txt(texto_a_guardar, nombre_archivo)
    else:
        print("Error al obtener el status de la pagina", response.status_code)
    while(True == True):
        response = requests.get(url)
        html = response.text
        nombre_archivo = "htmlanterior.txt"
        resultado = comparar_htmls(nombre_archivo, html)
        if resultado == True:
            print("La pagina sigue igual")
        else:
            print("La página se ha modificado!!")
            mostrar_ventana_emergente("La página ha sido modificada!!")
        time.sleep(5)

if __name__ == '__main__': 
    main()