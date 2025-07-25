

# Bucle for:
'''

Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los giros o vueltas del bucle que verifica las condiciones.

Imagina que el cuerpo del bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el buce while para hacerlo, puede tener el siguiente aspecto:

i = 0
while i < 100:
    # do_something()
    i +=

Sería bueno si alguien pudiera hacer esta cuenta aburrida por ti. ¿Es eso posible?
Por supuesto que lo es - hay un bucle especial para este tipo de tareas. y se llama for.

En realidad, el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento. Te mostraremos como hacerlo pronto, pero por ahora presentaremos una variante más sencilla de su aplicación.

for i in range(100):
    # do_something()
    pass

Importante:
-La palabra reservada for abre el bucle for; nota - No hay condición despés de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
-cualquier variable después de la palabra reservada for es la "variable de control" del bucle; cuenta los giros del bucle y lo hace automáticamente.
-La palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.
-La función range() es responsable de generar todos los valores deseados de la variable de control; en el ejemplo anterior, la función creará  o podemos decir que alimentara al bucle con valores subsiguientes del siguiente conjunto: 0,1,2,..97,98,99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso antes del valor de su argumento.
-Nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una "instrucción vacia" - la colocamos aquí por que la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto if, elif, else y while expresan lo mismo).

Los siguientes ejemplos serán un poco más modestos en el número de repeticiones de bucle.
'''

# Ejemplo 1: bucle for imprimiendo del 0 al 9
for i in range(10):
    print("El valor de i es: ", i)
print("Fin del programa..")
'''
Nota:
-EL bucle se ha ejecutado diez veces (es el argumento de la función range()).
-El valor de la última variable de control es 9(no 10, ya que comienza desde 0, no desde 1).
'''


# La invocación de la función range() puede ser equipada con dos argumentos, no solo uno.
for i in range(2, 8):
    print("El valor de i es: ", i)
print("Fin del programa..")
'''

-En este caso, el primer argumento determina el valor inicial (primero) de la variable de control.
-El último argumento muestra el primer valor que no se asignará a la variable de control.
-Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.
Su salida es: El primer valormostrado es 2 (tomando el primer argumento de la función range()).
El último es 7 (aunque el segundo argumento de la función range() es 8).

'''

