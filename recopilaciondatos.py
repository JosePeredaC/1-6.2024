#Desarrollado por AXDAE
#Proposito del codigo : Busca recopilar la información de la página websecgen.unmsm.edu.pe usando bs4, los datos son almacenados en carpetas con la información ordenada
import requests
import os
from bs4 import BeautifulSoup
codIn = int(input("Inserta el codigo con el que deseas empezar: "))
codfIn = int(input("Inserta el codigo con el que deseas terminar: "))
while codIn <= codfIn:
    url='http://websecgen.unmsm.edu.pe/carne/carne.aspx'
    data = {
		'ctl00$ContentPlaceHolder1$txtUsuario': str(codIn),
		'__VIEWSTATE': '/wEPDwULLTEzNzI1Nzc1MTAPZBYCZg9kFgICBA9kFgICBA9kFgICAQ9kFgJmD2QWCAIDDw8WAh4JTWF4TGVuZ3RoZmRkAh4PPCsADQBkAiIPDxYEHjZOb0JvdF9SZXNwb25zZVRpbWVLZXlfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSROb0JvdDEGAlf7kAE83EgeNE5vQm90X1Nlc3Npb25LZXlLZXlfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSROb0JvdDEFRE5vQm90X1Nlc3Npb25LZXlfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSROb0JvdDFfNjM4NDUxMjI0NTg0NzkyNTc4ZBYCAgEPFgIeD0NoYWxsZW5nZVNjcmlwdAUZJ2NIYUxsRW5HZScudG9VcHBlckNhc2UoKWQCJg8WGh4RQ3VsdHVyZURhdGVGb3JtYXQFA0RNWR4WQ3VsdHVyZVRpbWVQbGFjZWhvbGRlcgUBOh4bQ3VsdHVyZVRob3VzYW5kc1BsYWNlaG9sZGVyBQEsHgtDdWx0dXJlTmFtZQUFZXMtUEUeFkN1bHR1cmVEYXRlUGxhY2Vob2xkZXIFAS8eDERpc3BsYXlNb25leQsphgFBamF4Q29udHJvbFRvb2xraXQuTWFza2VkRWRpdFNob3dTeW1ib2wsIEFqYXhDb250cm9sVG9vbGtpdCwgVmVyc2lvbj0xLjAuMjAyMjkuMjA4MjEsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MjhmMDFiMGU4NGI2ZDUzZQAeDkFjY2VwdE5lZ2F0aXZlCysEAB4KQWNjZXB0QW1QbWgeE092ZXJyaWRlUGFnZUN1bHR1cmVoHhlDdWx0dXJlRGVjaW1hbFBsYWNlaG9sZGVyBQEuHhZDdWx0dXJlQU1QTVBsYWNlaG9sZGVyBQlhLm0uO3AubS4eIEN1bHR1cmVDdXJyZW5jeVN5bWJvbFBsYWNlaG9sZGVyBQNTLy4eDklucHV0RGlyZWN0aW9uCymKAUFqYXhDb250cm9sVG9vbGtpdC5NYXNrZWRFZGl0SW5wdXREaXJlY3Rpb24sIEFqYXhDb250cm9sVG9vbGtpdCwgVmVyc2lvbj0xLjAuMjAyMjkuMjA4MjEsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MjhmMDFiMGU4NGI2ZDUzZQBkGAEFJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkZ3ZFc3RhZG9DYXJuZQ9nZDmFIxTmbiHwPxODq7KkKhMdMi/7',
		'__EVENTVALIDATION': '/wEWCQKYnNGMBAKnqqeUBAKikZQ3AvmukKoFAu2+tNsDAu7ClKsEArOCz7YHAsmmlswJAtHui4oEP2SlMkc+SlC56KpLJSmV6YaKeLA=',
		'ctl00$ContentPlaceHolder1$cmdConsultar': 'Consultar'
	}
    response = requests.post(url, data=data)    
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find(id='ctl00_ContentPlaceHolder1_txtFacultad').get('value') == None:
        codIn += 1
        continue
    valor_codEs = soup.find(id='ctl00_ContentPlaceHolder1_txtUsuario')['value']
    valor_facu = soup.find(id='ctl00_ContentPlaceHolder1_txtFacultad')['value']
    valor_esc = soup.find(id='ctl00_ContentPlaceHolder1_txtPrograma')['value']
    valor_alum = soup.find(id='ctl00_ContentPlaceHolder1_txtAlumno')['value']
    imagen_codEs = soup.find(id='ctl00_ContentPlaceHolder1_imgAlumno')['src']
    reallinkimg = f"http://websecgen.unmsm.edu.pe/carne/{imagen_codEs}"
    directorio_destino = r'C:\Users\USER\OneDrive\Documentos\MIS CODIGOS\PYTHON\ELIMINAR'
    nombre_imagen = f'{valor_codEs}.jpg'
    ruta_archivo = os.path.join(directorio_destino, nombre_imagen)
    img_response = requests.get(reallinkimg)
    with open(ruta_archivo, 'wb') as f:
        f.write(img_response.content)
    print(valor_codEs,valor_facu,valor_esc,valor_alum)    
    print(f"Imagen de {valor_codEs} ha sido descargado con exito!")
    
    codIn+=1