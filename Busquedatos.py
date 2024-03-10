#Desarrollado por Axdae
#Proposito del codigo : Busca hacer consultas en la página de dni-peru.com 
from bs4 import BeautifulSoup
import requests
import time
import os
opcion = int(input("Elija la opción que desea utilizar:\n[1]Buscar DNI con Nombres y apellidos\n[2]Fecha de nacimiento con DNI\n[3]Apellidos y nombres por DNI\n[4]Edad por DNI\n[5]Salir\nEscoja una opcion: "))
os.system('cls')
while(opcion != 5):
    os.system('cls')
    match opcion:
        case 1:
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
            resultado = soup.find(class_="result-item").text
            print(resultado)
            os.system('PAUSE')
            os.system('cls')
            opcion = int(input("Elija la opción que desea utilizar:\n[1]Buscar DNI con Nombres y apellidos\n[2]Fecha de nacimiento con DNI\n[3]Apellidos y nombres por DNI\n[4]Edad por DNI\n[5]Salir\nEscoja una opcion: "))
            continue
        case 2:
            DNI = int(input("DNI: "))
            url='https://dni-peru.com/fecha-de-nacimiento-con-dni/'
            data = {
                'dni': str(DNI),
                'submit': 'Consultar'
            }
            response = requests.post(url, data=data)    
            soup = BeautifulSoup(response.text, 'html.parser')
            resultado = soup.find(class_="styled-form").text
            print(resultado)
            os.system('PAUSE')
            os.system('cls')
            opcion = int(input("Elija la opción que desea utilizar:\n[1]Buscar DNI con Nombres y apellidos\n[2]Fecha de nacimiento con DNI\n[3]Apellidos y nombres por DNI\n[4]Edad por DNI\n[5]Salir\nEscoja una opcion: "))
            continue
        case 3:
            DNI = int(input("DNI: "))
            url='https://dni-peru.com/buscar-dni-nombres-apellidos/'
            data = {
                'dni4': str(DNI),
                'buscar_dni': '',
                'submit': 'Buscar'
            }
            headers = {
                'Referer':'ttps://dni-peru.com/buscar-dni-nombres-apellidos/'
            }
            response = requests.post(url, data=data, headers=headers)    
            soup = BeautifulSoup(response.text, 'html.parser')
            resultado = soup.find(class_="mensaje4").text
            print(resultado)
            os.system('PAUSE')
            os.system('cls')
            opcion = int(input("Elija la opción que desea utilizar:\n[1]Buscar DNI con Nombres y apellidos\n[2]Fecha de nacimiento con DNI\n[3]Apellidos y nombres por DNI\n[4]Edad por DNI\n[5]Salir\nEscoja una opcion: "))
            continue
        case 4:
            DNI = int(input("DNI: "))
            url='https://dni-peru.com/saber-edad-con-dni/'
            data = {
                'dni7': str(DNI),
                'edad': 'Buscar'
            }
            headers = {
                'Referer':'https://dni-peru.com/saber-edad-con-dni/'
            }
            response = requests.post(url, data=data, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            resultado = soup.find(class_="resultado").text
            print(resultado)
            os.system('PAUSE')
            os.system('cls')
            opcion = int(input("Elija la opción que desea utilizar:\n[1]Buscar DNI con Nombres y apellidos\n[2]Fecha de nacimiento con DNI\n[3]Apellidos y nombres por DNI\n[4]Edad por DNI\n[5]Salir\nEscoja una opcion: "))
            continue
        case defecto:
            print("La opción que has elegido no esta contemplada entre las opciones :)")
            time.sleep(3)
            opcion = int(input("Elija la opción que desea utilizar:\n[1]Buscar DNI con Nombres y apellidos\n[2]Fecha de nacimiento con DNI\n[3]Apellidos y nombres por DNI\n[4]Edad por DNI\n[5]Salir\nEscoja una opcion: "))
            os.system('cls')
            continue
        