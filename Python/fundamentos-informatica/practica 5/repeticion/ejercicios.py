# Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número
# introducido por teclado por el usuario.

num = int(input("Ingrese numero a multiplicar: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


# Ejercicio 2: Escribir un programa que calcule la sumatoria desde 0 hasta m, donde m es
# un número introducido por la persona usuaria desde el teclado.
m = int(input("Ingrese numero a sumar: "))
for i in range(0, m):
    print(f"{m} + {i} = {m + i}")
    
# Ejercicio 3: Escribir un programa que muestre la tabla de los códigos ASCII. Los códigos
# ASCII van de 0 a 255

for i in range(0, 256):
    print(f"{i} = {chr(i)}")

# Ejercicio 4: Escribir un programa que lea letras del teclado indefinidamente hasta que el
# usuario ingrese “fin” e imprima el código ASCII de las mismas.

letras = input("Ingrese una letra del teclado: ")
while letras != "fin":
    print(ord(letras))
    letras = input('Ingrese una letra del teclado o escribir "fin" para salir: ')

print("Ha salido del programa")

# Ejercicio 5: Escribir un programa que calcule el promedio de N números ingresados por el
# usuario. (AYUDA: al comenzar el programa debe preguntar la cantidad de números a
# ingresar, luego iterar y leer tantos números del teclado como se indicó al inicio.)

cantidad = float(input("Cuantos numeros va a ingresar? :"))
contador = 0
numero = 0
while contador < cantidad:
    num = float(input("Ingrese un numero: "))
    numero = numero + num
    contador = contador + 1

cuenta = numero / cantidad
print(cuenta)
# se hace con el while


# Ejercicio 6: Escriba un programa que lea nombres de personas hasta que se ingrese el nombre “zzz”.
# Debe imprimir la cantidad de nombres que comienzan con “A”.

nom = str(input("Ingrese un nombre: "))
nombres = 0
while nom != "zzz":
    if nom[0] == "a" or nom[0] == "A":
        nombres = nombres + 1
        print(nombres)
    nom = str(input("Ingrese un nombre: "))


# Ejercicio 8: Escriba un programa que reciba del usuario su nombre, apellido y patente hasta que ingrese AAA,
# e imprima si está exento de impuesto o no.
# Tener en cuenta que los autos cuyas patentes empiezan con R, S y T no deben pagar impuesto.

nombre = (input("ingrese un nombre: "))
while nombre != "AAA":
    apellido = input("Ingrese un apellido: ")
    patente = input("Ingrese la patente: ")
    if patente[0] == "R" or patente[0] == "S" or patente[0] == "T":
        print("Usted esta exento de impuesto")
    elif patente[0] != "R" or patente[0] != "S" or patente[0] != "T":
        print("Debe pagar impuesto")
    nombre = input("Ingrese nombre o AAA para terminar: ")
    if nombre == "AAA":
        print("Finalizo el programa")

"""---------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------"""

"""Ejercicio 17:
a) Definir una función que permita el ingreso de números por teclado hasta ingresar el 0,
y retorne esa lista.
b) Definir una función que reciba como parámetro una lista de números y retorne como
resultado el promedio.
c) Definir una función que reciba como parámetro una lista de números y retorne como
resultado la suma de los números.
d) Definir una función que reciba como parámetro una lista de números y retorne el
número más grande de la lista (máximo).
e) Definir una función que reciba como parámetro una lista de números y retorne el
número más pequeño de la lista (mínimo).
f) Definir una función denominada porcentaje, que tenga 2 parámetros formales, que
representan el total y un valor y retorna el porcentaje de ese valor respecto del total."""

#a)
def armoLista():
    num = int(input("Ingrese un numero: "))
    lista = []
    while num != 0:
        lista.append(num)
        num = int(input("Ingrese otro numero o '0' para terminar: "))  
    return lista
#b)
def promedio_lista(lista):
    cuenta = 0
    for i in lista:
        cuenta = cuenta + i
    promedio = cuenta / len(lista)
    return promedio
#c) 
def sumar_lista(lista):
    cuenta = 0
    for i in lista:
        cuenta = cuenta + i
    return cuenta
#d)
def maximo_lista(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo
#e)
def minimo_lista(lista):
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return minimo
#f)
def porcentaje(total, valor):
    porcentaje = (valor * 100) / total
    return porcentaje

""" Utilizar las funciones definidas anteriormente para construir un programa que permita elegir una opción del siguiente menú, el cuál debe mostrarse permanentemente hasta que se
elija la opción 7:
1. Ver el promedio de los números
2. Ver la suma de los números
3. Ver la cantidad de números
4. Ver el número máximo
5. Ver el número mínimo
6. Calcular porcentaje
7. Salir """

print("1. Ver el promedio de los números")
print("2. Ver la suma de los números")
print("3. Ver la cantidad de números")
print("4. Ver el número máximo")
print("5. Ver el número mínimo")
print("6. Calcular porcentaje")
print("7. Salir")

opcion = int(input("Ingrese una opcion: "))
while opcion != 7:
    if opcion == 1:
        print("promedio de los números")
        lista1 = armoLista()
        print("El promedio de los numeros es: " + str(promedio_lista(lista1)))
    elif opcion == 2:
        print("suma de los números")
        lista1 = armoLista()
        print("La suma de los numeros es: " + str(sumar_lista(lista1)))
    elif opcion == 3:
        print("cantidad de números")
        lista1 = armoLista()
        print("la cantidad de numeros son: " + str(len(lista1)))
    elif opcion == 4:
        print("numero maximo")
        lista1 = armoLista()
        print("El numero maximo es: " + str(maximo_lista(lista1)))
    elif opcion == 5:
        print("numero minimo")
        lista1 = armoLista()
        print("El numero minimo es: " + str(minimo_lista(lista1)))
    elif opcion == 6:
        print("calcular porcentaje")
        v = int(input("ingrese el valor a promediar"))
        t = int(input("ingrese el total: "))
        print("El promedio de los numeros ingresados es: " + str(porcentaje(v,t)))
    else:
        print("Opcion incorrecta, vuelva a intentarlo")
    print("1. Ver el promedio de los números")
    print("2. Ver la suma de los números")
    print("3. Ver la cantidad de números")
    print("4. Ver el número máximo")
    print("5. Ver el número mínimo")
    print("6. Calcular porcentaje")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))

print("USTED A FINALIZADO EL PROGRAMA")

"""---------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------------------"""