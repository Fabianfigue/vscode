def cargar_datos():
    cont = 0
    lista = []
    while cont != 2:
        nom = input("Ingrese nombre del pais: ")
        cantOro = int(input("Ingrese cantidad de medallas de oro: "))
        cantPlata = int(input("Ingrese cantidad de medallas de plata: "))
        cantBronce = int(input("Ingrese cantidad de medallas de bronce: "))
        lista.append([nom, cantOro, cantPlata, cantBronce])
        cont = cont + 1
    return lista

lista_medallero = cargar_datos()

def calcular_puntaje(lista_medallero):
    lista = []
    for a in lista_medallero:
        puntaje = (a[1] * 3) + (a[2] *2) + (a[3] * 1)
        lista.append([a[0], puntaje])
    return lista

def mas_medallas(lista_medallero):
    cont = 0
    for i in lista_medallero:
        cuenta = (i[1] + i[2] + i[3])
        if cont < cuenta:
            cont = i[0]
    return cont

def cant_medallasO(lista_medallero, cant):
    cant = int(input("Introduzca una cantidad a buscar: "))
    cont = 0
    for i in lista_medallero:
        if i[2] == cant:
            cont = cont + 1

print("1- Cargar datos")
print("2- Calcular puntajes")
print("3- Quien tiene mas medallas")
print("4- Buscar medallas de oro" )
print("5- Salir")

opcion = int(input("Introduzca una opcion del menu: "))

while opcion != 5:
    if opcion == 1:
        print(cargar_datos(lista_medallero))
    elif opcion == 2:
        print(calcular_puntaje(lista_medallero))
    elif opcion == 3:
        print(mas_medallas(lista_medallero))
    elif opcion == 4:
        print(cant_medallasO(lista_medallero, 5))
    else:
        print("Error en la opcion, vuelva a intentar")
    print("1- Cargar datos")
    print("2- Calcular puntajes")
    print("3- Quien tiene mas medallas")
    print("4- Buscar medallas de oro" )
    print("5- Salir")
    opcion = int(input("Introduzca una opcion del menu: "))