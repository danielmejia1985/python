### Operadores Aritmeticos ###

print("\nOperadores Aritmeticos")
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

"""
En python no se pueden hacer operaciones aritmeticas con cadenas de caracteres, lo que si se puede hacer es imprimir tantas veces que uno desee una cadena de caracter utilizando el operador aritmetico de multiplicar, y se pueden unir 2 cadenas de caracteres con el operador aritmetico de suma, es decir una concatenación.
"""
# Esto mostrara por consola tres veces la cadena hola, hola hola hola
print("hola " * 3)

# Esto mostrara por consola la siguiente concatenación Hola Python
print("Hola " + "Pyhton")



### Operadores de Comparación ###
    
print("\nOperadores de Comparación")
print(3 > 4)# False
print(3 < 4)# True
print( 3 >= 4)# False
print(4 <= 4)# True
print(3 == 4)# False
print(3 != 4)# True

# Operadores de comparaciòn con cadena de caracteres

print("\nOperadores de comparación con cadena de caracteres")
print("hola" > "python")
print("aaaa" >= "aaaa")# Compara ordenación alfabética por ASCII --> True
print(len("aaaa") >= len("aaaa"))# Compara, cuenta caracteres --> True


### Operadores Logicos ###

"""

En Python, la lógica booleana se basa en dos valores: True (verdadero) y False (falso). Estos valores se utilizan para evaluar expresiones lógicas y tomar decisiones en el código. Python proporciona los siguientes 3 operadores lógicos para combinar(and), invertir(not) o comparar(or) expresiones booleanas.

1.- and --> Devuelve True si ambas expresiones son True
2.- not --> Invierte el valor booleano de una expresión
3.- or --> Devuelve True si al menos una de las expresiones es True
  

Concepto clave: El tipo de dato bool eb Python representa valores de verdad, ya sean True o False

Es importante entender la logica booleana el cual rige toda la programación

Uso en Estructuras de Control:
Los booleanos sonfundamentales para las estructuras if, while, y for, permitiendo ejecutar bloques de código condicionalmente

EN RESUMEN: la lógica booleana en Python es esencial para el control de flujo y la toma de decisiones en la programación. Los valores True y False, junto con los operadores lógicos, permiten construir expresiones complejas y evaluar condiciones para ejecutar diferentes partes del código.
"""

print("\nOperadores Logicos")


