#Ejercicio 2: Escribir un programa que calcule la sumatoria desde 0 hasta m, donde m es
#un número introducido por el usuario desde el teclado.

m = int(input('Introduzca un numero que quiera sumar: '))

for i in range(m):
    print(f'{i} + {m} = {i + m}')