# Importante: Todos los ejercicios de la práctica deben ser implementados usando funciones.

# Ejercicio 1: Definir una función que reciba como parámetro un número e imprima por pantalla si es positivo, negativo o cero. Utilice esta función para escribir un programa que lee un número ingresado por el usuario y muestre si es positivo, negativo o cero.

def es_positivo(num):
    if num > 0:
        print("Es positivo")
    elif num == 0:
        print("Es positivo")
    else:
        print("Es negativo")

# Ejercicio 2: Escribir una función que lea dos números “n” y “m” y determine si n es divisible por m, mostrando el siguiente mensaje por pantalla: “El número n es/no es divisible por m”. Reemplazar n y m por los números correspondientes.

def es_divisible(n, m):
    if n % m == 0:
        print(n / m)
    else:
        print("El número n es/no es divisible por m")

# Ejercicio 3: Escribir un programa que me indique si un número es divisible por 6, mostrando un mensaje por pantalla: “El número xx elegido es/no es divisible por 6” Nota: Debe hacerlo usando la función definida en el ejercicio anterior.

number = input("Ingrese un numero: ")
cuenta = number % 6
if es_divisible(number, 6) == 0:
    