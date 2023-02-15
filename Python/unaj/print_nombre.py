#Escriba un programa que lea nombres de personas hasta que se ingrese el
#nombre “zzz”. Debe imprimir la cantidad de nombres que comienzan con “A”.
carpeta = []
nom = str(input('Introduzca un nombre: '))

while nom != 'zzz':
    if nom[0] == 'a' or 'A':
        print(nom)
    nom = str(input('Introduzca un nombre: '))