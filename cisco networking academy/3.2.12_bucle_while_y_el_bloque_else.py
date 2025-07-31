import os
os.system("clear")

# El bucle while y el bloque else
''''
Ambos bucles while y for, tienen una caracteristica interesante (y rara vez se usa).

Te mostraremos como funciona-intenta juzgar por ti mismo si es utilizable.

En otras palabras, trata de convencerte si la función es valiosa y útil, o solo es azúcar sintáctica. Echa un vistazo al fragmento en el editor. Hay algo extraño al final - la palabra reservada else. Como pudiste a ver sospechado, los bucles también pueden tener la rama else, como los if.

La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.
'''

# Ejemplo while con else.
print("Ejemplo bucle while con sentencia else..")
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else: ",i)

# Ejemplo for con else.
print("Ejemplo bucle for con sentencia else..")
for i in range(5):
    print(i)
else:
    print("else: ", i)


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)