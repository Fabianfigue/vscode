#Definir una función que reciba como parámetro una lista de números y retorne como
#resultado la suma de los números.
lista = [1, 2, 3, 4, 5]


def suma_numeros(lista):
    suma = 0
#suma un conjunto de valores en una lista.
    for i in lista:
        suma += i
    
    return suma

print("la suma de su lista es: ", suma_numeros(lista))