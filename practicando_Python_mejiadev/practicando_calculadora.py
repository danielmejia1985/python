import os
os.system("clear")


print("Bienvenido a la caculadora de Python...")

# Ingresando un valor entero desde el teclado.
valor_entero_1 = int(input("Por favor ingrese un valor entero: "))
print("valor ingresado: ", valor_entero_1)
print("1-sumar | 2-restar | 3-multiplicar | 4-dividir")
opcion_aritmetica = int(input("Seleccione una operación aritmetica: "))
if opcion_aritmetica == 1:
    print("Selecciono sumar")
    valor_entero_2 = int(input("Ingrese el 2do. valor para sumarlo: "))
    print("El resultado es: ", valor_entero_1 + valor_entero_2)

print("Fin del programa")