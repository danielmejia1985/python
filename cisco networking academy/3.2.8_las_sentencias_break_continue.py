from ctypes.wintypes import LARGE_INTEGER
import os
from unicodedata import numeric
os.system("clear")
# Las sentencias break y continue
'''

Hasta ahora, hemos tratado el cuerpo del bucle como una secuencia indivisible  e inseparable de instrucciones que se realizan completamente en cada giro del bucle. Sin embargo, como desarrollador, podrias enfrentar las siguientes opciones:

-Parece que no es necesario continuar el bucle en su totalidad; se debe abstener de seguir ejecutando el cuerpo del bucle e ir más allá.
-Parece que necesitas comenzar el siguiente giro del bucle sin completar la ejecución del turno actual.

Python proporciona dos instrucciones especiales para la implementación de estas dos tareas. Digamos por razones de precisión que su existencia en el lenguaje no sea necesaria - un programador experimentado puede codificar cualquier algoritmo si estas instrucciones.

Tales adiciones, que no mejoranel poder expresivo del lenguaje, si no que solo simplifican  el trabajo del desarrollador, a veces se denomina, dulces sintácticos o azúcar sintáctica.

Estas dos instrucciones son:
-break: Sale del bucle inmediatamente, e incodicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
-continue: Se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión se prueba de inmediato.

Ambas palabras son palabras claves reservadas.

Ahora mostraremos dos ejemplos simples para ilustrar como funcionan las dos instrucciones.
'''


# Ejemplo 1, break
print('La instrucción \"break\"')
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle: ", i)
print("fuera del bucle.")


# Ejemplo 2, continue
print('\nLa instruccion \"contunue\"')
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle", i)
print('Fuera del bucle.')

# Las sentencias break y continue: más ejemplos
'''
Regresamos a nuestro programa que reconoce el más grande de los números ingresados. Lo convertiremos dos veces, usando las instrucciones de break y continue.
'''

# Ejemplo con la sentencia break
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number
if counter != 0:
    print("El numero más grande es: ", largest_number)
else:
    print("No has ingresado nungun número..")


# Ejemplo con la sentencia continue
largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es: ", largest_number)
else:
    print("No has ingresado nungun número..")
    