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
