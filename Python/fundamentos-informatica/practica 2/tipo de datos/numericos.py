#ejercicios de la practica 2 (3 al 12)

#       ejercicio 3: Pedir que se ingrese un número e imprimir el triple

from http.client import PRECONDITION_FAILED
from mailbox import NoSuchMailboxError
from time import altzone


num = int(input("ingresar el numero a multiplicar * 3: ")) #pedimos al usuario ingresar un numero y lo forzamos a que sea un entero con "int"
calcu = num * 3 # creamos una nueva variable para hacer la cuenta y guardar su resultado
print (calcu) # imprimimos en pantalla el resultado de la variable calcu

#       ejercicio 4: Pedir que se ingrese un número e imprimir la mitad

num = int(input("Ingresar un numero para dividirlo en 2: ")) #pedimos al usuario ingresar un numero con input y forzamos que sea un entero con "int"
calcu = num / 2 # creamos la varia ble que guarda nuestro resultado de la cuenta
print (calcu) #imprimimos el resultado de la cuenta que hicimos en linea 11.

#       ejercicio 5: Pedir que se ingrese 3 notas e imprimir el promedio. Recordar que el promedio es la suma de los números dividido la cantidad.

#pedimos ingresar los 3 numeros a promediar
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

#creamos la variable promedio, donde procedemos a hacer la cuenta, separando en terminos
promedio = (nota1 + nota2 + nota3) / 3

#imprimimos en pantalla el resultado de promedio
print (promedio)

#      ejercicio 6: Pedir base y altura de un triángulo y mostrar el área del mismo
#pedimos al usuario los datos del triangulo
base = int(input("ingrese base del triangulo: "))
altura = int(input("ingrese altura del triangulo: "))

#creamos la variable area para realizar la cuenta
area = base * altura
#imprimimos en pantalla el resultado
print(area)

#       ejercicio 7: Pedir el diámetro de un círculo y calcular su área y perímetro. Recordarque Perímetro = π * Diámetro , Área = π * radio2. Por último, el diámetro = 2 * radio

diametro = int(input("Ingrese diametro del circulo: "))
radio = diametro / 2
area = 3.14 * radio**2
perimetro = 3.14 * diametro

print(area)
print(perimetro)

#       ejercicio 8: Pedir 2 números y mostrar la división entre ellos y el resto.

num1 = int(input("Ingrese un numero a dividir: "))
num2 = int(input("Ingrese el otro numero a dividir: "))

dividir = num1 / num2
resto = num1 ** num2

print("Esta es la division: ", dividir, ". Este es el resto: ", resto)


#       ejercicio 9: Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad de litros que tiene. (saber que 1000 cm3=1 litro)

alto = int(input("Ingrese el alto de la pileta en cm: "))
ancho = int(input("Ingrese el ancho de la pileta en cm: "))
largo = int(input("Ingrese el largo de la pileta en cm: "))

volumen = alto * ancho * largo
cantL = volumen / 1000


#       ejercicio 10: Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar (son de 60x60 cm)

ancho = int("Ingrese el ancho del terreno en metros: ")
largo = int("Ingrese el largo del terreno en metros: ")

result = (ancho * largo) / 0.36
print (result)

#       ejercicio 11: Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar cuánto se gasta por cada producto y el total
producto1 = input("Ingrese el primer producto: ")
cantidad1 = int(input("ingrese la cantidad: "))
precio1 = float(input("ingrese precio del producto por unidad: "))

producto2 = input("Ingrese el segundo producto: ")
cantidad2 = int(input("ingrese la cantidad: "))
precio2 = float(input("ingrese precio del producto por unidad: "))

producto3 = input("Ingrese el tercer producto: ")
cantidad3 = int(input("ingrese la cantidad: "))
precio3 = float(input("ingrese precio del producto por unidad: "))

producto4 = input("Ingrese el cuarto producto: ")
cantidad4 = int(input("ingrese la cantidad: "))
precio4 = float(input("ingrese precio del producto por unidad: "))

gastos1 = ("por " + str(producto1) + " se gasta: " + str(precio1) + "$")
gastos2 = ("por " + str(producto2) + " se gasta: " + str(precio2) + "$")
gastos3 = ("por " + str(producto3) + " se gasta: " + str(precio3) + "$")
gastos4 = ("por " + str(producto4) + " se gasta: " + str(precio4) + "$")

totalGastos = precio1*cantidad1 + precio2*cantidad2 + precio3*cantidad3 + precio4*cantidad4

print(gastos1)
print(gastos2)
print(gastos3)
print(gastos4)
print("El total de los gastos es de: " + str(totalGastos))

#       ejercicio 12: Diseña un programa que, a partir del valor del lado de un cuadrado (3metros), muestre el valor de su perímetro (en metros) y el de su área (en metroscuadrados). (El perímetro debe darte 12 metros y el área 9 metros cuadrados.)



#       ejercicio 15: Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir). 

verbo = input("ingrese un verbo en infinitivo(terminan con ar, er o ir): ")

print(verbo[-2:])

# Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión bajo y de su año de nacimiento) y mostrarla.

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
fechaNac = str(input("Ingrese su fecha de nacimiento en el siguiento formato 00/00/0000: "))

clave = (nombre[0] + apellido[0] + fechaNac[-4:])
print(clave)

#   Ejercicio Nuevo: Crear una lista con palabras, luego pedir al usuario que ingrese una nueva palabra, ingresarla a la lista e imprimir la cantidad de elementos que tiene la lista. Usando la función len.

hardware = ["monitor", "mouse", "teclado"]

hardware.append(input("Ingrese un componente del hardware a la lista: "))

print(len(hardware))