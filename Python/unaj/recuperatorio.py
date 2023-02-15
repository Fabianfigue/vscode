lista = []
def cargar_personas():
    cont = 0
    while cont < 4:
        nom = input('ingrese un nombre: ')
        edad = input('ingrese la edad: ')
        lista.append([nom, edad])
        cont += 1
    return print(lista)

cargar_personas()

def coincide_personas(lista, edad):
    for edad in lista:
        if edad == lista:
            return print(f'{edad}')

coincide_personas(lista, edad=20)
def nombre_existeOno(lista, nombre):
    if nombre in lista:
        return True
    else:
        return False


def nombre_mas_de_cinco(lista):
    if len(lista[edad]) > 5:
        return sum(lista) / len(lista)