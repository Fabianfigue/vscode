#Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir un
#programa que muestre el número más alto.

lista = [1, 14, 56, 43, 23, 46, 58, 123, 67 ]

alto = lista[0]

for i in range(0, len (lista)):
    if lista[i] > alto:
        alto = lista [i]

print('El numero mas alto de la lista es: ', alto)