#Definir una función que reciba como parámetro una lista de números y retorne como
#resultado el promedio.
lista = [1, 2, 3, 4, 5, 6, 5]


def promedio_numeros(lista):
    return sum(lista) / len(lista) #promedio de la suma de la totalidad de numeros guardados en la lista

#invoco la funcion agregando la lista que quiero pasar por ella
print(promedio_numeros(lista))