# Análisis de muestras de ćodigo
"""

Ahora mostraremos algunos programas simples pero completos. No los explicaremos a detalle, porque consideramos que los comentarios (y los nombres de las variables) dentro del código son guias suficientes.

Todos los programas resuelven el mismo problema - encuentran el número mayor de una serie de números y lo imprimen.
"""

# Ejemplo 1: Comenzaremos con el caso más simple - ¿cómo identificar el mayor de los dós números?

print("Ejemplo 1:")
# Se leen dos números
number_1 = int(input("Ingresa el primer número: "))
number_2 = int(input("Ingresa el segundo número: "))

# Se elige el número más grande
if number_1 > number_2:
    larger_number = number_1
else:
    larger_number = number_2

# Se imprime el resultado
print("El número más grande es: ", larger_number)

# El fragmento de código anterior debe estar claro - lee dos valores enteros, los compara y encuentra cuál es el más grande.

# Ejemplo 2: Es hora de complicar el código - encontremos el mayor de los tres números. 
print("Ejemplo 2: ")
#Se leen los tres números
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))

if number1 > number2:
    number_mayor = number1
elif number2 > number3:
    number_mayor = number2
else:
    number_mayor = number3
print("EL numero mayor es: ", number_mayor)