#Escribir un programa que muestre la tabla de multiplicar de un número
#introducido por teclado por el usuario.
numero = int(input('Ingrese un numero: '))

for i in range(1,11):
    print (f'{i} x {numero}= {i*numero}')