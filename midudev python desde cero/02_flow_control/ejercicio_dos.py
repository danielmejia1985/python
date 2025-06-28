"""
        
Ejercicio 2: Calculadora simple.
Pedir al usuario dos números y una operación (+, -, *, /), realizar la operacion y muestra el resultado (manejar la división entre cero)
"""

import os
os.system("clear")


print("Ejercicio Dos.. -Calculadora Simple-")

numero_uno = int(input("Ingrese valor uno: "))
numero_dos = int(input("Ingrese valor dos: "))
print("Seleccione una operación aritmética")
print("\n 1.-Suma \n 2.- Resta \n 3.- Multiplicación \n 4.- División")
operacion_aritmetica = int(input("Número de operación aritmetica: "))

if operacion_aritmetica == 1:
   print("Selecciono SUMAR")
   print(f"Resultado: {numero_uno + numero_dos}")

elif operacion_aritmetica == 2:
    print("Selecciono RESTAR")
    print(f"Recultado: {numero_uno - numero_dos}")
elif operacion_aritmetica == 3:
    print("Selecciono MULTIPLICAR")
    print(f"Resultado: {numero_uno * numero_dos}")
elif operacion_aritmetica == 4:
    print("Selecciono DIVIDIR")
    try:
        print(f"Resultado: {numero_uno / numero_dos}")
    except ZeroDivisionError:
        print("Error. No se puede dividir entre cero")