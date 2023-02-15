#Escribir un programa que calcule el promedio de N números ingresados por el
#usuario. (AYUDA: al comenzar el programa debe preguntar la cantidad de números a
#ingresar, luego iterar y leer tantos números del teclado como se indicó al inicio.)

num = int(input('cuantos numeros va a ingresar? '))

suma = 0
numero = 0

for numero in range(num):
    numero = int(input('Ingrese un numero? '))
    suma += numero
    promedio = suma / num

print(f'El promedio de numeros ingresados es: {promedio}')