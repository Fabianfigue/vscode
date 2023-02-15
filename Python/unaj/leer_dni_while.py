#Escriba un programa que lea números de documentos de identidad de
#personas hasta que se ingrese el número “999”. Debe imprimir la cantidad de números de
#documentos menores que 20.000.000.

#pedir al usuario que ingrese un dni para comenzar
dni = int(input('ingrese numero dni'))

#solo entra al while si el numero no es 999
while dni != 999:
    #entra a la condicion solo si el numero de dni es menos que 20.000.000
        if dni < 20000000:
            print(dni)
        dni = int(input('ingrese numero dni'))