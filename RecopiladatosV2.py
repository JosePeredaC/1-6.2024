import re
import requests
from bs4 import BeautifulSoup
import os 

def menu():
    codIn = int(input("Inserta el codigo con el que deseas empezar: "))
    codfIn = int(input("Inserta el codigo con el que deseas terminar: "))
    codi = codIn
    while codIn <= codfIn:
        conexion(codi)
        codi+=1
def conexion(cod):
    url='http://websecgen.unmsm.edu.pe/carne/carne.aspx'
    data = {
		'ctl00$ContentPlaceHolder1$txtUsuario': str(cod),
		'__VIEWSTATE': '/wEPDwULLTEzNzI1Nzc1MTAPZBYCZg9kFgICBA9kFgICBA9kFgICAQ9kFgJmD2QWCAIDDw8WAh4JTWF4TGVuZ3RoZmRkAh4PPCsADQBkAiIPDxYEHjZOb0JvdF9SZXNwb25zZVRpbWVLZXlfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSROb0JvdDEGEDtZCzmB3EgeNE5vQm90X1Nlc3Npb25LZXlLZXlfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSROb0JvdDEFRE5vQm90X1Nlc3Npb25LZXlfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSROb0JvdDFfNjM4NTI3MzI5MTYzMjgzOTg0ZBYCAgEPFgIeD0NoYWxsZW5nZVNjcmlwdAUZJ2NIYUxsRW5HZScudG9VcHBlckNhc2UoKWQCJg8WGh4RQ3VsdHVyZURhdGVGb3JtYXQFA0RNWR4WQ3VsdHVyZVRpbWVQbGFjZWhvbGRlcgUBOh4bQ3VsdHVyZVRob3VzYW5kc1BsYWNlaG9sZGVyBQEsHgtDdWx0dXJlTmFtZQUFZXMtUEUeFkN1bHR1cmVEYXRlUGxhY2Vob2xkZXIFAS8eDERpc3BsYXlNb25leQsphgFBamF4Q29udHJvbFRvb2xraXQuTWFza2VkRWRpdFNob3dTeW1ib2wsIEFqYXhDb250cm9sVG9vbGtpdCwgVmVyc2lvbj0xLjAuMjAyMjkuMjA4MjEsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MjhmMDFiMGU4NGI2ZDUzZQAeDkFjY2VwdE5lZ2F0aXZlCysEAB4KQWNjZXB0QW1QbWgeE092ZXJyaWRlUGFnZUN1bHR1cmVoHhlDdWx0dXJlRGVjaW1hbFBsYWNlaG9sZGVyBQEuHhZDdWx0dXJlQU1QTVBsYWNlaG9sZGVyBQlhLm0uO3AubS4eIEN1bHR1cmVDdXJyZW5jeVN5bWJvbFBsYWNlaG9sZGVyBQNTLy4eDklucHV0RGlyZWN0aW9uCymKAUFqYXhDb250cm9sVG9vbGtpdC5NYXNrZWRFZGl0SW5wdXREaXJlY3Rpb24sIEFqYXhDb250cm9sVG9vbGtpdCwgVmVyc2lvbj0xLjAuMjAyMjkuMjA4MjEsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MjhmMDFiMGU4NGI2ZDUzZQBkGAEFJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkZ3ZFc3RhZG9DYXJuZQ9nZO/0y3jg2RwRuVITg1biQb7ilGwF',
		'__EVENTVALIDATION': '/wEWCQK4uNdUAqeqp5QEAqKRlDcC+a6QqgUC7b602wMC7sKUqwQCs4LPtgcCyaaWzAkC0e6LigRgW34mP0Svme3Hf+FH67InbiFOKQ==',
		'ctl00$ContentPlaceHolder1$cmdConsultar': 'Consultar'
	}
    response = requests.post(url, data=data)    
    soup = BeautifulSoup(response.text, 'html.parser')
    procesotexto(soup)
def procesotexto(html):
    try:
        valor_codEs = html.find(id='ctl00_ContentPlaceHolder1_txtUsuario')['value']
        valor_facu = html.find(id='ctl00_ContentPlaceHolder1_txtFacultad')['value']
        valor_esc = html.find(id='ctl00_ContentPlaceHolder1_txtPrograma')['value']
        valor_alum = html.find(id='ctl00_ContentPlaceHolder1_txtAlumno')['value']
        print(f"Alumno {valor_codEs}:\n")
        print(f"\tNombres y apellidos: {valor_alum}")
        print(f"\tFacultad: {valor_facu}")
        print(f"\tEscuela: {valor_esc}")
        imagen_codEs = html.find(id='ctl00_ContentPlaceHolder1_imgAlumno')['src']
        reallinkimg = f"http://websecgen.unmsm.edu.pe/carne/{imagen_codEs}"
        directorio_destino = r'C:\Users\USER\OneDrive\Documentos\RECUPERADOS\asd'
        nombre_imagen = f'{valor_codEs} {valor_alum}.jpg'
        ruta_archivo = os.path.join(directorio_destino, nombre_imagen)
        img_response = requests.get(reallinkimg)
        with open(ruta_archivo, 'wb') as f:
            f.write(img_response.content)
        print(f"Imagen de {valor_codEs} ha sido descargado con exito!")
    except:
        print("Ha ocurrido un error al recopilar los datos del alumno")
def procesoimg(html):
    pass
def evasion():
    pass
def hilos():
    pass

def main():
    menu()
if __name__ == '__main__': 
    try:
        main()
    except:
        print("\nSe ha salido del programa")