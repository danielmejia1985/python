# Bucle while
#
# En python, un bucle while se utiliza para repetir un bloque de código mientras se cumpla una condición, es muy útil cuando no sabes de atemano cúantas veces se debe repetir algo.
# Sintaxis
# while condicion:
    # Código que se ejecuta mientras la condición sea verdadera

import os
os.system("clear")




# Ejemplo 1: Contar del 1 al 5, el bucle se repite mientras la variable contador sea menor o igual a 5.
contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1





# Ejemplo 2: Solicitar contraseña hasta que sea correcta.
# En este segundo ejemplo, el bucle sigue pidiendo la contraseña hasta que se teclea la correcta es decir evulua que la variable contraseña no es igua a (!=) "python123", en este caso dicha condición da True por la variable contraseña tiene asignado un str vacio y se ejecuta el cuerpo del bucle es decir solicitando contraseña, si el usuario ingresa una contraseña que no es igua a "python123" seguira dando True y seguira ejecutando el cuerpo del bucle, hasta que se ingrese "python123" y saldra del bucle para ejecutar la ultima línea que es imprimir en pantalla "¡Contraseña Correcta!". 
contraseña = ""

while contraseña != "python123":
    contraseña = input("Ingrese una contraseña: ")
print("¡Contraseña Correcta!")




# Ejemplo 3: Bucle infinito (con break para salir).
# En este caso el bucle while siempre ejecutara su cuerpo de còdigo ya que su condicón es un booleano con valor True, dicho cuerpo de bucle solicita escribir 'salir' a su vez sera evualuada con la sentencia if y si da True se ejecuta el cuerpo del if que es la instrucción break y se rompera la ejecución del bucle infinito, si el usuario teclea algo diferente a 'salir' estara ejecutandose el cuerpo del bucle.

while True:
    texto = input("Escribe 'salir' para terminar: ")
    if texto == "salir":
        break
print("Escribiste:", texto)




# Ejemplo 4: Usar while con else.
# En este ejemplo tenemox la variable x inicializada con el valor entero 3, la condición del bucle resultara True ya que tres es mayor que cero y al ejecutar el cuerpo del bucle while mostrara en pantalla el valor 3 seguido le restara 1 con la sentencia x -= 1 que es lo mismo que (x = x -1), esto se repetira hasta que x sea cero y la condición del bucle de False puesto que cero no es mayor que cero, posteriormente se ejecutara el else.
x = 3
while x > 0:
    print(x)
    x -= 1
else:
    print("¡Cuenta regresiva finalizada!")
