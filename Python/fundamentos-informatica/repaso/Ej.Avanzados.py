# """Ejercicio 1:
# a) Defina una función que reciba como argumento una cadena de texto y retorne un
# valor entero indicando la cantidad de vocales que contiene la cadena Ejemplo:
# “agua” -> 3, “pepe” ->2
# b) Defina una función que genere una lista de palabras hasta que se ingrese la
# palabra “fin” la cual NO debe ser almacenada en la lista, por cada palabra,
# también se guardara la cantidad de vocales que contiene la misma, para esto
# deberá utilizar la función definida en el punto 1) a, al finalizar la función deberá
# retornar la lista generada.
# a) La lista resultado deberá tener una estructura similar a:
# 1) [[“uno”,2],[ “pepe”,2],[”agua!”,3],…etc]
# c) defina una función que reciba como argumento la lista generada en el punto 1.b) e
# imprimir las palabras que tienen mas de 3 vocales.
# d) escriba el código del programa que integra las 3 funciones antes definidas."""

# def cantidad_vocales(cadena):
#     return '"'+ cadena[:] + '"' + " -> " + str(len(cadena))

# def crear_lista():
#     palabra = input("ingrese palabra para agregar a la lista: ")
#     lista = []
#     while palabra != "fin":
#         ult_vocal = cantidad_vocales(palabra)
#         lista.append([palabra, ult_vocal[-1]])
#         palabra = input("ingrese otra palabra o fin para salir: ")
#     return lista

# lista1 = str([])
# lista1 = print(crear_lista())
# def palabras_vocales(lista):
#     for a in lista:
#         if "a" in a[0] or "e" in a[0]:
#             print(a)

# palabras_vocales(lista1)

"""
a) Realice un programa para manejar equipos de fútbol, Armar una lista que tenga
información sobre los equipos de fútbol. Para cada equipo deberán tener: el
nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor.
b) Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los
equipos que están en la primera y última posición de la lista.
c) Imprimir el nombre del equipo Campeón de la lista generada en el punto a), el
equipo campeón es aquel que sumo más puntos."""

def armarEquipos():
    lista = []
    nombre = input("Como se llama el equipo? ")
    puntaje = int(input("Agregar puntaje: "))
    goles = int(input("Cuantos goles tiene: "))
    lista.append([nombre, puntaje, goles])
    return lista

print("1. Cargar equipos:")
print("2. Salir")

opcion = int(input("ingrese una opcion: "))

while opcion != 2:
    if opcion == 1:
        print(armarEquipos())
    else:
        print("La opcion ingresada es incorrecta. Vuelva a intentarlo: ")
        
    print("1. Cargar equipos:")
    print("2. Salir")
    opcion = int(input("ingrese una opcion: "))

print("USTED A SALIDO DEL PROGRAMA")
print("ADIOS")


