#Inicializo contador mayores de edad
contM = 0
#Realizo lectura del primer nombre
nom = input('ingrese nombre: ')
#Comienzo proceso de lectura y calculo
while nom != 'zzz':
    #Ingrese nombre, apellido y edad
    ape = input('Ingrese apellido: ')
    edad = int(input('Ingrese edad: '))

    #evaluo la edad
    if edad >= 18:
        contM= contM + 1
    #vuelvo a leer otro nombre
    nom = input('ingrese nombre: ')

#Imprimo cantidad de mayores de 18
print('Cantidad de personas mayores de 18 son: ', contM)