#Escribir un programa que lea letras del teclado indefinidamente hasta que el
#usuario ingrese “fin” e imprima el código ASCII de las mismas.

valores = []
letras = str(input('Ingrese una letra '))

while letras != 'fin':
    valores.append(letras)
    print(ord(letras))
    letras = str(input('Ingrese una letra '))