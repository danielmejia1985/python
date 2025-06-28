"""
01 - Sentencias condicionales (if, elif, else)
Permite ejecutar bloques de código solo si se cumplen ciertas condiciones.

"""
import os
os.system("clear")

print("\n Sentencia simple condicional")

edad = 19
if edad >= 18:
    print("Eres mayor de edad")

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print(f"Eres mayor de edad")
else:
    print("Eres menor de edad")
    
print("\n Sentencia condicional con elif")
calificacion = 5

if calificacion >= 9:
    print("Sobresaliente")
elif calificacion >= 7:
    print("Notable")
elif calificacion >= 6:
    print("Aprobado")
else:
    print("No está parobado")

# Operador logico and.- en el if se tienen que cumplir ambas comparaciones como True para ejecutar el código  dentro del if, si uno no se cumple se ejecuta else.
    

# Operador logico or.- en el if se tienen que cumplir una comparación o otra como True para ejecutar el código dentro del if.
print("\n Condicionales múltiples o Operadores logicos and, or")
edad = 17
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puede conducir")
    
if edad >= 18 or tiene_licencia:
    print("Puedes conducir")
else:
    print("Eres menor de edad pero con permiso puedes conducir")

# Operador logico not.- Con este operador logico negamos el valor asignado a dicha variable, es decir si es True con not ahora sera False.
print("\n Operador logico not")
nombre_variable = False

if not nombre_variable:
    print("Se ejecuta if por que la condición fue True")
else:
    print("Se ejecuta else por que la condición fue False")
    

# Condionales anidadas, entre más anidadas sean, más complejo puede ser el código.  
print("\n Anidar condicionales")


# Condición ternaria.- es una forma concisa de u if-else en una línea de código.
print("\n La condicioón ternaria:")




