# seccion 2 - Bucles en Python

"""

En la segunda sección, aprenderas acerca de los bucles en Python y especificamente - los bucles while y for. Aprenderás a cómo crear (y evitar caer en) en bucles infinitos, cómo salir de bucles, y omitir ciertas iteraciones en los bucles.

Bucles en tú código con while.

Sentencia presentada:
mientras haya algo que hacer
    hazlo

En python, un bucle se puede representar de la siguiente manera
while
    instruction

Se observa algunas similitudes con la instrcción if, está bien. De hecho, la diferencia sintáctica es solo una: la palabra reservada while en lugar de la palabra reservada if.

La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.

Nota: todas las reglas relacionadas con sangria tambíen se aplican aquí.

Algoritmo de while:
while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    .
    .
    .
    .
    instruction_n


Es importante recordar que:
-Si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) poner sangría a todas las instrucciones de la misma manera.
-Una instrucción o conjunto de instrucciones ejecutadas dentro de while se llama cuerpo del bucle.
-Si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, el cuerpo no se ejecuta ni una sola vez (ten encuenta la analogía de no tener que hacer nada si no hay nada que hacer).
-El cuerpo debe poder cambiar el valor de la condición, por que si la condición es True al principio, el cuerpo podría funcionar continuamente hasta el infinito. Observa que hacer una cosa generalmente disminuye la cantidad de cosas por hacer.
"""

# Un bucle infinito
"""

Un bucle infinito, tambén denominado bucle sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente (bucle sin fin).

Ejemplo: El siguien bucle no puede finalizar su ejecución
while True:
    print("Estoy atrapado dentro de un bucle.")
"""


# Ejemplo de bucle.
# Almacena el actual número más grande aqui.
largest_number = -99999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Si si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escriba -1 para detener: "))

# Imprime el número más grande.
print("EL número más grande es: ", largest_number)