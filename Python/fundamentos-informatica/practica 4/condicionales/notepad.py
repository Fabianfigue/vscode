# Ejercicio 2: Escribir una función que lea dos números “n” y “m” y determine si n es divisible por m, mostrando el siguiente mensaje por pantalla: “El número n es/no es divisible por m”. Reemplazar n y m por los números correspondientes.

def es_divisible(n, m):
    if int(n) % int(m) == 0:
        print(int(n) / int(m))
    else:
        print("El número n no es divisible por m")

# Ejercicio 3: Escribir un programa que me indique si un número es divisible por 6, mostrando un mensaje por pantalla: “El número xx elegido es/no es divisible por 6” Nota: Debe hacerlo usando la función definida en el ejercicio anterior.

number = input("Ingrese un numero: ")
cuenta = int(number) % 6
if cuenta == 0:
    print("El número " + str(number) + " es divisible por 6")
else:
    print("El número " + str(number) + " no es divisible por 6")