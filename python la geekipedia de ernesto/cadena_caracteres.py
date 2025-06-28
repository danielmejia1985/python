#En programación, las cadenas de caracteres o mejor conocidas como Strings, es una serie de caracteres compuestas 
#por letras, números, signos y símbolos, que dentro de sus funciones, destaca la interacción de programa con el usuario

"""
En python, existen distintas operaciones para manipular una cadena de caracteres (Strings). Dentro de las cuales se encuentras:
.La asignación
.La concatenación
.La búsqueda
.La extracción
.La comparación

"""




#La asignación, consiste en asignar una cadena de caracteres a otra, para lo cual es necesario utilizar el operador +=
"""
El operador += nos indica que va a sumar sin sobreescribir el valor de la variable, es decir toma el valor de la variable más lo que le va asignar es decir.

mensaje = "Hola"
mensaje += "Daniel" --> esto queire decir que a la variable mensaje le estamos sumando o concatenando el valor Daniel ahora el nuevo valor de la variable mensaje es: HolaDaniel

Nota: Si no podemos el caracter +,  lo que vamos hacer es definir la variable con un nuevo valor dejando solo el caracter de asignación =

mensaje = "Hola"
mensaje += " "
mensaje += "Daniel Mejia"
print(mensaje)

"""

#La concatenación, es una operación que consiste en unir dos cadenas o más, para formar una cadena de mayor tamaño.
"""
Para lo cual es necesario utilizar el operador +

mensaje = "Hola"
espacio = " "
nomnbre = "Daniel"
print(mensaje + espacio + nomnbre)
"""


#La búsqueda, consiste en localizar dentro de una cadena, una subcadena más pequeña a un carácter.
"""
Para lo cual es necesario utilizar el método find, este metodo devuelve un valor entero que seria el valor del espacio donde empieza la cadena de caracteres que a encontrado. 

Tener en cuenta que las cadenas de caracteres empieza a contar desde la posición cero.

mensaje = "Hola Daniel"
busqueda_caracteres = mensaje.find("Daniel") 
print(busqueda_caracteres)
"""


#La extracción
"""
La extracción, se trata de sacar fuera de una cadena, una porción de la misma según su posición dentro de ella.
Para ello es necesario indicar la posición a extraer [1:8]

mensaje = "Hola Daniel"
extraer_subcadena = mensaje[1:8] 
print(extraer_subcadena) 
#ola Dan

Como obserbación, el rango de los corchetes quiere decir que desde donde va empezar a extraer y despues de los 2 puntos es el final de de hasta donde va extraer, pero seria un caracter antes de la ultima posición.
"""


#La comparación
"""
La comparación, se utiliza para comparar dos cadenas de caracteres.

Para ello se utiliza el operador doble igual, == 

mensaje_uno = "Hola"
mensaje_dos = "Hola" 
print(mensaje_uno == mensaje_dos) --> Esto imprimira por pantalla True ya que ambas variables son iguales en su valor y si fuera diferente  el resultado seria False es decir un valor boolaneo.

"""

mensaje_uno = "Hola"
mensaje_dos = "hola" 
print(mensaje_uno == mensaje_dos)
