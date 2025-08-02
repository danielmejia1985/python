import os
os.system("clear")

print("Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. \n")

parte_antes = ""

for i in "john.smith@pythoninstitute.org":
    if i == "@":
        break
    else:
        parte_antes += i
    print("correo antes del @:", parte_antes)
