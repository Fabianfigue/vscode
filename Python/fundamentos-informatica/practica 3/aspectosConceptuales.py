"""
a) ¿Qué ventajas tiene la utilización de funciones?
    reutilizacion de codigo, sin tener que volver a reescribirlo

b) ¿Hay algún cuidado en el orden en el que se pasan los parámetros a una función?
    #si, ya que si pasamos por otro orden nos lo toma como un parametro diferente al que vamos a necesitar

c) ¿Cuándo uso la sentencia return?
    #cuando necesito que la funcion retorne y al final de la funcion.

d) ¿Qué diferencia hay entre la definición y la invocación de una función? 
    una definicion de funcion tiene parametros formales, y el codigo que va a ser llamado en la invocacion

e) ¿Qué son los parámetros formales y para qué sirven? Ejemplifique.
    """#los parametros formales se definen en la definicion de funcion, estos sirven para declarar los usos de la funcion. ej:
def esMayorQue(num1 ,num2): #parametro formal
    return num1 > num2

"""
f) ¿Qué son los parámetros reales y para qué sirven? Ejemplifique."""
    #los parametros reales se definen en el programa, fuera de la identacion de la funcion, sirven para invocar a los parametros formales desde el programa principal. ej: 

print(esMayorQue(5,4)) #parametros reales
"""

g) ¿Qué es el cuerpo de una función? Ejemplifique.
""" #El cuerpo de una funcion es todo lo que esta identacion luego de la definicion y de invocado los parametros formales ej: 

def cuerpoDeFuncion():
    print("Este texto es parte de una funcion, si lo estas viendo es por que me invocaron")

"""

h) ¿Existen funciones sin parámetros o argumentos?
    si

i) ¿Puede usar una letra o un número como parámetro formal? ¿Y como parámetro real?
    si, puede usarse de las dos maneras

j) ¿Puedo tener una cantidad distinta de parámetros formales que reales en una función?
    no, tienen que tener la misma cantidad para que la funcion funcione

k) ¿Cómo se puede implementar un módulo con solo definiciones de funciones e importarlo desde tu programa? ¿Cuáles son las formas de importar que ofrece Python?
    import math 
    from {modulo} import {variable} 

l) ¿Qué diferencias hay entre los siguientes códigos?
    """
    # i) import math #para importar el modulo completo de matematica
    # ii) from math import sqrt #para importar solamente la raiz cuadrada del modulo matematica