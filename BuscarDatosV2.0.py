    #!/usr/bin/env python
#_*_ coding: utf8 _*_
#Desarrollado por AXDAE
#Proposito recavar la maxima información posible de la web inicialmente usando como fuente a paginas como dni-peru.com 
import requests
import time
import os
import re

from bs4 import BeautifulSoup

def menu():
    os.system("cls")
    print("******Busqueda de datos******")
    print("[0]Salir")
    print("[1]Busqueda por nombre")
    print("[2]Busqueda por DNI")
    opcion = int(input("\tDigite la opción a usar ---> "))
    match(opcion):
        case 0:
            exit()
        case 1:
            porNombre()
        case 2:
            porDNI()

def porNombre():
    nombres = str(input("Nombres: "))
    apellidoP = str(input("Apellido paterno: "))
    apellidoM = str(input("Apellido materno: "))
    url='https://dni-peru.com/buscar-dni-por-nombre/'
    data = {
        'nombres': str(nombres),
        'apellido_paterno': str(apellidoP),
        'apellido_materno': str(apellidoM),
        'search-button': 'Buscar'
    }
    response = requests.post(url, data=data)    
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        resultado = soup.find(class_="result-item").text
        regex1 = (r"\d")
        findDNI = re.search(regex1, resultado)
        imprimir1 = findDNI.group()
        regex2 = (r"\b[A-Z]+\s[A-Z]+,[A-Z]+\s[A-Z]+\b")
        findNombres = re.search(regex2, resultado)
        imprimir2 = findNombres.group()
        print(f"DNI: {imprimir1}\n")
        print(f"Nombres y apellidos: {imprimir2}")

    except:
        print("Ha ocurrido un error")
def porDNI():
    DNI = int(input("DNI: "))
    url='https://dni-peru.com/buscar-dni-nombres-apellidos/'
    data = {
        'dni4': str(DNI),
        'buscar_dni': '',
        'submit': 'Buscar'
    }
    headers = {
        'Referer':'https://dni-peru.com/buscar-dni-nombres-apellidos/'
    }
    response = requests.post(url, data=data, headers=headers)    
    soup = BeautifulSoup(response.text, 'html.parser')
    resultado = soup.find(class_="mensaje4").text
    regex = (r"Nombres:\s*([A-ZÁÉÍÓÚÜÑ\s]+)\s*Apellido\s*Paterno:\s*([A-ZÁÉÍÓÚÜÑ\s]+)\s*Apellido\s*Materno:\s*([A-ZÁÉÍÓÚÜÑ\s]+)")
    findNombres = re.search(regex,resultado)
    nombres = findNombres.group(1)
    apellido_paterno = findNombres.group(2)
    apellido_materno = findNombres.group(3)
    nombre_completo = nombres + ", " + apellido_paterno + " " + apellido_materno
    print("Nombres y apellidos:", nombre_completo)
    time.sleep(5)
    url='https://dni-peru.com/fecha-de-nacimiento-con-dni/'
    data = {
        'dni': str(DNI),
        'submit': 'Consultar'
    }
    headers = {
        'Referer':'https://dni-peru.com/fecha-de-nacimiento-con-dni/'
    }
    response = requests.post(url, data=data, headers=headers)    
    soup = BeautifulSoup(response.text, 'html.parser')
    resultado = soup.find(class_="styled-form").text
    regex = (r"\d{2}/\d{2}/\d{4}")
    findNacimiento = re.search(regex,resultado)
    imprimir = findNacimiento.group()
    print(f"Fecha de nacimiento: {imprimir}")
def main(): 
    menu()
 
if __name__ == '__main__': 
    main()
    