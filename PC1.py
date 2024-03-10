import os
import time  
import math
print("[1]Calcular la suma de resistencias en serie o paralelo\n[2]Calcular de la raiz quinta de ((x^7+5)^5+x^5)\n[3]Determinar cuanto recibe cada carrera por la donación especial\n[4]Salir")
while True:
    opcion=int(input("Escoja la opción que desea realizar: "))
    match opcion:
        case 1: 
            print("Introduzca los valores de la reistencia 1, 2 y 3 sucesivamente: \n")        
            resistencia = float(input(f"Introduce el valor de la resistencia [1]: "))
            resistencia2 = float(input(f"Introduce el valor de la resistencia [2]: "))
            resistencia3 = float(input(f"Introduce el valor de la resistencia [3]: "))          
            paralelo = (resistencia*resistencia2*resistencia3)/(resistencia2*resistencia3+resistencia*resistencia3+resistencia*resistencia2)
            serie = resistencia+resistencia2+resistencia3
            print(f"El valor de la sumatoria es:\nSerie :{serie}\nParalelo :{paralelo}")
            os.system("PAUSE")
            os.system("cls")
        case 2:
            print("Introduce el valor de x en la ecuación ((x^7+5)^5+x^5)")
            valorX=int(input("X = "))
            resultado=(((valorX**7)+5)**5+(valorX**5))
            print(f'El resueltado de la operación es: {resultado}')
        case 3:
            print("Ingrese el monto de la donación que recibiran las E.P")
        case 4:
            print("Saliendo...")
            time.sleep(3)
            break
        case _: 
            print("Valor incorrecto")
            os.system("cls")
            time.sleep(3)
