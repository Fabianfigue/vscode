#Definir una función que permita el ingreso de números por teclado hasta ingresar el 0,
#y retorne esa lista.

def ingresar_numeros():
    lista = []
    numero = int(input('ingrese un numero: '))
    while numero != 0:
        lista.append(numero)
        numero = int(input('ingrese un numero: '))
    print(lista)

ingresar_numeros()