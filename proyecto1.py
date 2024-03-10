import webbrowser
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pyautogui 
import pyautogui as pg

print("""       .:c;''..       ...,:lodxxxxo.    
      .:l:,'..        ...';:clodxxd,    
,''...;oc;'....  ..  ....',;:ccllll;    
;,'.....''',,;;:::;:::::::cccllcc;,..   
',.. .'codo;.'',;::clllooooooddddl:'.   
 ....c00doc'..........',;;:clloddxxo:,..
    .k0oc,.    ....... .........','','''
    .odxo.        .....'.       ...     
    .,lko'.       .,,''c:.      ,o,     
    .:lxl,,''.....;;.. .okc,..';k0;     
    .'lo,.''.... .'. .. ,Ox:',cckXx.    
     .',''''...  .'...,.,kOl'..;lxl.    
      ..,;.. .,..,,'.,xkxOKd. 'c,       
        ...  ':,..,clldkxxOd..c;        
       .';l, ,:'.'.,l:coolxd'co.        
     ...'lOo;oo,.. ....,::okk0o.        
    ..   ,dOOOd,.    .'.;ox0K0l         
  ..   .''.'lo;'....'lOkxOOOx:.         
...  ..;;.  'c;''....'cxOkl,','.        
,.  .',;'   .;'... .,,;;c,  .,:;.       
""")
print("Elija la función que desea usar:\n1.Buscar información\n2.Buscar nickname\n3.\n4.\n5.")
opcion= int(input("Introduce la opción a elegir: "))
def buscarInfo(busqueda):
    try:
     driver = webdriver.Chrome()
     driver.get('https://www.google.com')
     texto = driver.find_element(By.NAME,'q')
     texto.send_keys(f'intext:"{busqueda}"')
     time.sleep(1.2)
     texto.send_keys(Keys.RETURN)
     time.sleep(5.2) 
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        if driver:
            driver.quit()
def buscarNick(busqueda2):
    try:
      os.system(cmd.exe)
    except Exception as e:
       print(f"Ha ocurrido un error: {e}")
if opcion == 1:
    busqueda=str(input("Introduce lo que necesitas buscar: "))
    buscarInfo(busqueda)
elif opcion == 2:
    busqueda2=str(input("Introduce el nickname que quieres buscar: "))
    buscarNick(busqueda2)