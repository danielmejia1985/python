import os
import time
os.system("clear")


#  Más acerca del bucle for y la función range() con tres argumentos
'''

La función range() también peude aceptar tres argumentos

for i in range(2, 8, 3):
    print("El valor de i es: ", i)

El tercer argumento es un incremento, es un valor agregado para controlar la variable en cada giro del bucle, el valor predeterminado del incremento es 1


'''

# Ejemplo 1
'''

Programa corto cuya tarea es escribir algunas de las primeras potencias de dos
'''
# power = 1
# for expo in range(16):
#     print("2 ala potencia de ", expo, "es ", power)
#     power *=2
# print("Fin del programa..")



# Ejemplo 2
''''

escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"

Utiliza el esqueleto que hemos proporcionado en el editor.
import time

# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

# Escribe una función print con el mensaje final.


  INFO EXTRA  
Ten en cuenta que el código en el editor contiene dos elementos que pueden no ser del todo claros en este momento: la sentencia import time y el método sleep(). Vamos a hablar de ellos pronto.

Por el momento, nos gustaría que supieras que hemos importado el módulo time y hemos utilizado el método sleep() para suspender la ejecución de cada función posterior de print() dentro del bucle for durante un segundo, de modo que el mensaje enviado a la consola se parezca a un conteo real. No te preocupes - pronto aprenderás más sobre módulos y métodos.
'''

for i in range(1, 6, 1):
    print(i,"Mississippi")
    time.sleep(1)
print("¡Listos o no, ahí voy!")
