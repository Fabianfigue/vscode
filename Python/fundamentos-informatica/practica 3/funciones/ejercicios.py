from cmath import pi
#Ejercicio 1:

# a) Dado el siguiente código indique cuáles son los parámetros reales y los formales:
    # a) Definicion de funciones
def sumaAlcuadrado(x, y):           #PARAMETROS FORMALES
    rta= x**2 + 2*x*y + y**2     
    return rta
#Programa principal
print ("Bienvenidos/as a la Suma al Cuadrado")
a=input("Ingrese el valor de a:")      #PARAMETROS REALES
b=input("Ingrese el valor de b:")      #PARAMETROS REALES
print (sumaAlcuadrado(a, b))           #PARAMETROS REALES


# b)Mencione los errores en los siguientes códigos. Justifique:
# a)      
def suma(par1, par2):
    print(par1+par2)
suma()  #ERROR NO PASA ARGUMENTOS PAR1, Y PAR2
# b) 
def suma(par1, par2):
    print (par1 + par2)
#        print(suma(12, 10)) #ERROR MAL IDENTADO. PRINT TIENE QUE LLAMAR A LA FUNCION FUERA DE ELLA
# c) 
def suma(par1, par2):
    return (par1 + par2)
#       suma(12, 10)    #ERROR LA FUNCION SE PIDE AFUERA
# d) 
def suma(par1):
    return (par1 + 2)
#suma(12, 10)          #ERROR LA FUNCION SOLO PIDE 1 ARGUMENTO Y SE PASAN 2

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 2:
# Definir una función denominada imprimir_mensaje que imprima el siguiente mensaje en pantalla: “Estudiando Fundamentos de Informática en la UNAJ”. No recibe ninguna información por lo tanto no tiene ningún parámetro formal.

def imprimir_mensaje():
    print("Estudiando Fundamentos de Informatica en la UNAJ")


"""---------------------------------------------------------------------------------------------------"""


#Ejercicio 3:
# Definir una función denominada retorno_mensaje que retorne siguiente mensaje: “Estudiando Fundamentos de Informática en la UNAJ”.
    # A. ¿Cómo hago para mostrar ese mensaje en pantalla?
    # B. ¿Qué diferencia encuentra con el ejercicio anterior?
    # C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAJ“ y “Estudiando Python en la UNAJ” utilizando la misma función ¿Cómo la modificarías?

def retorno_mensaje():
    return "Estudiando Fundamentos de Informatica en la UNAJ"

#a)
print(retorno_mensaje())

#b) Puedo imprimir el codigo cuando lo deseo en el programa principal y no cuando la funcion sea llamada

#c) 
def retorno_mensaje(a):
    return a

x = input("Ingrese mensaje: ")
print(retorno_mensaje(x))

"""---------------------------------------------------------------------------------------------------"""

# Ejercicio 4:
# Definir una función denominada imprimo_fecha que reciba tres cadenas de caracteres como parámetros formales, que representan un día, un mes y un año e imprima la fecha de la siguiente manera: “ 21 de septiembre de 2021”.

def imprimo_fecha(cad1, cad2, cad3):  #PARAMETROS FORMALES
    print(cad1 + " de " + cad2 + " de " + cad3)

dia = input("Ingrese dia: ")
mes = input("Ingrese un mes: ")
año = input("Ingrese un año: ")

imprimo_fecha(dia, mes, año)

"""---------------------------------------------------------------------------------------------------"""

# Ejercicio 5
#  Definir una función denominada cuantos_dias que reciba el número de mes como parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1), debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31], [“febrero”, 28], ...]

def cuantos_dias(numMes):
    lista = [["enero", 31], ["febrero", 28], ["marzo", 31], ["abril", 30], ["mayo", 31], ["junio", 30], ["julio", 31], ["agosto", 31], ["septiembre", 30], ["octubre", 31], ["noviembre", 30], ["diciembre", 31]]
    x = lista[numMes-1][1]
    return x

"""---------------------------------------------------------------------------------------------------"""

# Ejercicio 6
# Definir una función que reciba un número como parámetro y mostrar la tabla de multiplicar de dicho número.

def tablaMultiplicarDe(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    print(num * 4)
    print(num * 5)
    print(num * 6)
    print(num * 7)
    print(num * 8)
    print(num * 9)
    print(num * 10)

tablaMultiplicarDe(3)

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 7: 
# Definir una función que calcule el área de un círculo, otra que calcule el área de un rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían recibir dichas funciones.

import math

def areaCirculo(radio):
    return math.pi * radio**2

def areaRectangulo(largo, ancho):
    return largo * ancho

def areaCuadrado(lado):
    return lado**2

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con el precio anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje rebajado.

def calculo_rebaja(num1, num2):
    porcentaje = (num1 * num2 / 100) + num1
    return porcentaje

numero1 = int(input("Ingrese el numero: "))
numero2 = int(input("Ingrese el porcentaje a aumentar al numero anterior: "))

print("El numero " + str(numero1) + " con el aumento de " + str(numero2) + "%" + " queda a: " + str(calculo_rebaja(numero1, numero2)))

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 9: Definir una función llamada calculo_nuevo_precio que reciba dos números,uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.

def calculo_nuevo_precio(num1, num2):
    cuenta = ((num1 * num2) / 100) + num1
    return cuenta
 
print(calculo_nuevo_precio(10, 5))

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 10: Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión sabiendo que cada salita es acompañada por tres adultos.

def calculo_transporte(sala1, sala2, sala3, asientos):
    adultos = 9
    cuenta = (adultos + sala1 + sala2 + sala3) / asientos
    return cuenta

alumnos1 = int(input("Ingrese cantidad de alumnos de 1era: "))
alumnos2 = int(input("Ingrese cantidad de alumnos de 2da: "))
alumnos3 = int(input("Ingrese cantidad de alumnos de 3ra: "))
cantAsientos = int(input("Ingrese cantidad de asientos del micro: "))

print("se necesitan contratar: " + calculo_transporte(alumnos1, alumnos2, alumnos3, cantAsientos))

"""---------------------------------------------------------------------------------------------------"""

#ejercicio 11
def armo_cartel(producto,preAnterior, preRebaja):
    print("*************************************")
    print("Atención!!! Gran rebaja para el producto: " + str(producto))
    print("antes: $" + str(preAnterior)) 
    print("ahora: $" + str(preRebaja))
   
numero = input("ingrese el nombre del producto: ")
precioAntes = input("ingrese el precio anterior del producto: ")
precioRebajado = input("ingrese el precio ya rebajado: ")

armo_cartel(numero, precioAntes, precioRebajado)

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 12: Definir una función llamada calculo_litros que reciba tres números, el alto, ancho y profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.
def calculo_litros(alto, ancho, profundidad):
    litrosCuenta = (alto + ancho + profundidad) * 1000
    return litrosCuenta

piletaAlto = int(input("ingrese alto de la pileta en metros: "))
piletaAncho = int(input("ingrese ancho de la pileta en metros: "))
piletaProfundidad = int(input("ingrese la profundidad de la pileta en metros: "))

print("la cantidad de litros de su pileta es de: ")
print(str((calculo_litros(piletaAlto, piletaAncho, piletaProfundidad))) + " L")

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le toca pagar a cada uno.

def a_pagar(cantPer, gastBebida, gastComida, alquiler):
    cuenta = (gastBebida + gastComida + alquiler) / cantPer
    return cuenta

"""---------------------------------------------------------------------------------------------------"""

#Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión respectiva.

def convertir_a_dolar(pesos):
    cuenta = pesos * 148.59
    return "El tipo de cambio a dolar es: " + str(cuenta) + " Dolares"
def convertir_a_euro(pesos):
    cuenta = pesos * 148.40
    return "El tipo de cambio a euro es: " + str(cuenta) + " Euros"
def convertir_a_real(pesos):
    cuenta = pesos * 28.76
    return "El tipo de cambio a real es: " + str(cuenta) + " Reales"

"""---------------------------------------------------------------------------------------------------"""

# Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.

def calculo_dosis(diasAsuministrar, cantXdia, cantComprimidos):
    return (cantComprimidos / cantXdia) <= diasAsuministrar

