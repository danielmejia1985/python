# Condiciones y ejecucioón condicional
"""

Ya sabes coo hacer preguntas a Python, pero aún no sabes coo hacer un uso razonable de las respuestas. Se debe tener un mecanismo que le permita hacer algo si se cumple una condición, y no hacerlo si no se cumple.

es como la vida real: haces ciertas cosas o no cuando se cumple una condición específica, por ejemplo, sales a caminar si el clima es bueno, o te quedas en casa si está húmedo y frío.

Para tomar tales decisiones, Python ofrece una instrucción especial. Debido a su naturaleza y su aplicación, se denomina instrucción condicional (o sentencia condicional).

Existen varias variantes de la misma. Comenzaremos con las más simple, aumentando la dificultad lentamente.

La primera forma de una sentencia condicional, que puede ver a continuación, está escrita de manera muy informal pero figurada:
    if true_or_not:
        do_this_if_true

Esta sentencia condicional consta de los sigueintes elementos, estrictamente necesarios en este orden:
.La palabara clave reservada if;
.Uno o más espacios en blanco;
.Una expresión (una pregunta o una respuesta) cuyo valor se interpreta únicamente en términos de True (cuando su valor no sea cero) y False (cuando sea igual a cero);
.Unos dos puntos seguidos de una nuevalínea;
.Una instrucción con sangría o un conjunto de intrucciones (se requiere absolutamente al menos una instrucción)


Estructura de la sentencia if, elif y else
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

"""