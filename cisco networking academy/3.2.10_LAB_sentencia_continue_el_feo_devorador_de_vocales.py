from http.client import CONTINUE
import os
os.system("clear")

#La sentencia continue - el Feo Devorador de Vocales.
'''
Escenario
La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin  ejecutar las sentencias dentro del bucle.

Se puede usar tanto con bucles while y for.

Tu tarera aquí es muy especial; Debes diseñar un devorador de vocales, escribe un programa que use:
-un bucle for
-el concepto de ejecución condicional (if-elif-else).
-la sentencia continue.

Tu programa debe:
-pedir al usuario que ingrese una palabra
-utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes.
-utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
-imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
'''

# Solicitud de palabra ingresada por el usuario y al mismo tiempo convirtiendola a mayúscula
palabra_ingresa_usuario = input("Por favor ingrese una palabra: ").upper()

for i in palabra_ingresa_usuario:
    if i == "A":
            continue
    elif i == "E":
          continue
    elif i == "I":
          continue
    elif i == "O":
          continue
    elif i == "U":
          continue
    else:
        print(i)
        





print("Fin del programa..")