import os
os.system("clear")

# QUIZ DE SECCIÓN

'''
Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.
'''

print("Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.")
for i in range(0, 11, 1):
    # Cuando el resto de i / 2 sea 1 se compara que no es igual que cero en el if y dara True, es así que entra el cuerpo del if e imprime en pantalla i es decir la iteración actual
    if i % 2 != 0:
        print(i)


print('Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla')
indice = 0

while indice <= 10:
    if indice % 2 != 0:
        print(indice)
    indice += 1




print("Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo")
