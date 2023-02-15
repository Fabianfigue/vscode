#Escriba un programa que reciba del usuario su nombre, apellido y patente
#hasta que ingrese AAA, e imprima si está exento de impuesto o no. Tener en cuenta que
#los autos cuyas patentes empiezan con R, S y T no deben pagar impuesto.

nom = str(input('Ingrese su nombre o "AAA" para salir: '))
ape= str(input('Ingrese su apellidoo "AAA" para salir: '))
pat= input('Ingrese su patente o "AAA" para salir: ')

impuesto = []
while nom != 'AAA':
    impuesto.append(pat)
    if impuesto[0] == 'R' or 'S' or 'T':
        print('No debe pagar ningun impuesto')
        nom = str(input('Ingrese su nombre o "AAA" para salir: '))
    else:
        print('Usted debe impuestos')