"""
Ejercicio 3: Año bisiesto.
Pedir al usuario que introduzca un año y determina si es bisiesto, un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400
"""

import os
os.system("clear")

print("Ejercicio Cuatro..")

year_number = int(input("Ingresar año: ")) 
bisiesto = year_number % int(4)

if bisiesto == 0:
    print("El año ingresado SI ES BISIESTO")
else:
    print("EL año ingresado NO ES BISIESTO")