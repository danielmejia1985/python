# Recorrer una lista de frutas con bucle while.

import os
os.system("clear")

# Explicación paso a paso
# - La variable frutas está inicializada con una lista de 4 elementos de tipo String.
# - La variable indice esta inizializada con el valor entero cero, y es el punto de partida del bucle while, esto quiere decir que la iteración empezara desde la posición cero.
# - len(frutas): Está función devuelve la cantidad de elementos en la lista, 4 en este caso.
# - El bucle while se ejecuta mientras la variable indice sea menor que la longitud de la lista.
# - En cada iteración el cuerpo del bucle muestra una fruta y luego le suma en 1 a la variable indice.
# - Cuando la condición del bucle sea False, es decir la variable indice ahora ya no es menor que la longitud de la lista, ejecutara lo que siga después del bucle, este caso imprime "Fin del programa..".
frutas = ["manzana", "plátano", "naranja", "pera"]
indice = 0

while indice < len(frutas):
    print("frutas:", indice, frutas[indice])
    indice += 1
print("Fin del programa..")




# Recorrer lista al revés.
# Explicación línea a línea.
# En la variable cadenas_str: Se crea una lista con 4 elementos de tipo String, desde la posición cero hasta la posición 3.
# En la variable indice_lista: Extraemos la longitud de la lista y le restamos uno asi la iteración comenzara desde "cadena_str: 4".
# En la condición del bucle while,  se ejecutara mientras el valor de la variable indice_lista sea mayor o igual que cero.
# Al ejecutarse el cuerpo del bucle while lo primero que ara es es mostrar en pantalla la el String "Cadena:", seguido del valor del incice actual es decir la ultima posición que es 3.
# En la lía de código donde: indice_lista -= 1, esto restara menos 1 para pasar a la posición anterior.
# Nota: La variable indice_lista en algun momento de la interación valdra -1 es decir ya no es mayor o igual que cero, puesto que la condición del bucle while sera False y dejara de ejecutar el cuerpo del bucle.
cadenas_str = ["cadena_str: 1", "cadena_str: 2", "cadena_str: 3", "cadena_str: 4"] 
indice_lista = len(cadenas_str) -1 # Empieza desde el último indice

while indice_lista >= 0:
    print("Cadena:", cadenas_str[indice_lista])
    indice_lista -= 1

