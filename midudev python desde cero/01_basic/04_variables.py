#Variables en Pyhton
"""
Las variables sirven para guardar datos en memoria.
Python es un lenguaje de tipado dinámico y de tipado fuerte

Asignar una variable solo falta poner el nombre de la variable = valor

nombre_variable = "hola"

Las variables se pueden reasignar en tiempo de ejecución, 

Tipado dinámico: el tipo de dato se determina en tiempo de ejecución que no tiene que ser declarado explícitamente, es decir  en la siguiente variable la estamos declarando como str o String sin decirle que tipo de dato es si no de manera automatica.

nombre_variable = "variable_tipo_str"


Tipado Fuerte: Python no realiza conversiones de tipo automática


Convenciones de nombres de variables: El nombre de las variables en python se usara la forma snake_case es decir separado por guiones bajos, como se muentra en el siguiente ejemplo.

mi_nombre_de_variable = valor


CONSTANTE en python: En python NO existe la constante pero por convención declaramos una variable con UPPER_CASE es decir todo en mayuscula  para definir que su valor es fijo y constante y tengamos la precaución de no reasignar el valor de dicha variable ya que se puede reasignar su valor como una variable como tal.


Nombre de variables NO validos: 
123456_variable = valor
mi-variable = valor
mi variable = valor
True = False

"""

mi_nombre = "daniel"
print(mi_nombre)