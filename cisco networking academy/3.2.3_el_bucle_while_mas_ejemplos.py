# Veamos otro ejemplo utilizando el bucle while. Sigue los comentarios para descubrir la idea y la solución


"""

Un programa que lee una secuencia de números y cuenta cuántos números son pares y cuántos son impares. El programa termina cuando se ingresa un cero.
"""

odd_numbers = 0
even_numbers = 0

# # Lee el primer número
# number = int(input("Introduce un número o escribe 0 para detener: "))

# # 0, termina la ejecución
# while number != 0:
#     # Verifica si el número es impar.
#     if number % 2 == 1:
#         # Incrementar el contador de núemros impares odd_numbers.
#         odd_numbers += 1 # Esta expresión es igual a decir: odd_numbers = odd_numbers + 1
#     else:
#         # Incrementa el contador de números pares even_numbers.
#         even_numbers += 1 # Esta expresión es igual a decir: even_numbers = even_numbers +1
    
#     # Lee el siguiente número.
#     number = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Conteo de números impares: ", odd_numbers)
# print("Conteo de números pares: ", even_numbers)


# Empleando una variable counter para salir del bucle.
counter = 5
while counter != 0:
    print("Dentro del bucle. ", counter)
    counter -= 1
print("Fuera del bucle. ", counter)

