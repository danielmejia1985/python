import os
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