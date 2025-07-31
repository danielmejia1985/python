# RESUMEN DE SECCIÓN

'''
Existen dos tipos de bucles en Python: while y for:

1: El bucle while ejecuta una sentencia o un conjunto de sentencias siempre que una condicón booleana especifica sea verdadera.

2: El bucle for ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia (por ejemplo, una lista, un diccionario, una tupla o un conjunto) u otros objetos que son iterables por ejemplos cadenas. Puedes usar bucle for para iterar sobre una secuencia de números usando la función incorporada range().

Puedes usar las sentencias breal y continue para cambiar el flujo de un bucle.

Los bucles while y for también pueden tener una cláusula else en Python. La cláusula else se ejecuta después de que el bucle finalice su ejecución siempre y cuando no haya terminado con break.

La función range() genera una secuencia de números. Acepta enteros y devuelve objetos de rango. La sintaxis de range() tiene el siguiente aspecto: range(start, stop, step), donde:

-start: es un parámetro opcional que especifica el número de inicio de la sencuencia (cero por defecto).
-stop: es un parámetro opcional que especifica el final de la secuencia generada (no está incluido).
-step: es un parámetro opcional que especifica la diferencia entre los números en la secuencia es (uno por defecto)
'''

word = "Python"
for letter in word:
    print(letter, end = "*")