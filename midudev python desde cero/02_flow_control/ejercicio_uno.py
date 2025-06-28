import os
os.system("clear")

"""
Ejercicio 1: Determinar el mayor de dos números. 
Pedir al usuario que intruduzca dos números y muestre un mensaje indicando cuál es mayor o si son iguales.

"""

print("Ejercicio Uno..")

numero_uno =  input("\n ingresar número 1: ")
numero_dos = input("\n ingresar número 2: ")

if numero_uno > numero_dos:
    print("\n" + "Número Uno" + " es mayor que " + "Número Dos")
elif numero_uno == numero_dos:
    print(" \n Ambos números son iguales")
    #print("\n" + "Número Uno" + " es igual a " + "Número Dos")
else:
    print("\n Operación no valida")