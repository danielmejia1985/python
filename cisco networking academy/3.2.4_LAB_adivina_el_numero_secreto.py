# Adivina el número secreto
"""

Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

pedirá al usuario que ingrese un número entero;
utilizará un bucle while;
comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."


INFO EXTRA  
Por cierto, observa la función print(). La forma en que lo hemos utilizado aquí se llama impresión multilínea. Puedes utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la lectura del texto o crear un diseño especial basado en texto. Experimenta con ello.

print('''
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# ''')

"""

import os
os.system("clear")

print("""
 +================================+
 | ¡Bienvenido a mi juego, muggle!|
 | Introduce un número entero     |
 | y adivina qué número he        |
 | elegido para ti.               |
 |¿Cuál es el número secreto?     |
 +================================+
""")

secret_number = 777

# Número ingresado por el usuario valor entero
numero_ingresado_usuario = int(input("Ingrese el número: "))
#print("El usuario ingreso: ", numero_ingresado_usuario)

while numero_ingresado_usuario != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

    # Ingresar nuevamente el número para adivinar cual es
    numero_ingresado_usuario = int(input("Ingrese nuevamente el número: "))

print("Número Secreto Correcto: ", numero_ingresado_usuario, "¡Bien hecho, muggle! Eres libre ahora.")
print("FIN DEL PROGRAMA.")