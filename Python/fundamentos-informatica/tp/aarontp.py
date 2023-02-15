def personajes():                                #equipos(paises) retorna lista con elementos(paises)
    # lista = [
    # ["boca", partidos ganados, partidos perdidos, empate, goles a favor, en contra]
    # ]
    
    lista = []
    print("Ingresar características de los personajes")
    vida = int(input("vida: "))
    while vida != 0:
        p_ataque = int(input("poder de ataque: "))
        p_defensa = int(input("poder de defensa: "))
        nombre = input("nombre: ")
        raza = input("raza: ")
        elemento = input("elemento: ")
        datos = (vida, p_ataque, p_defensa, nombre, raza, elemento)
        lista.append(datos)
        vida = int(input("vida: "))
    return lista

def dobledaño(lista):                            #ganador_por_goles_max
    # que equipos hicieron mas goles que la media
    lista_dd = []
    for pj_uno in lista:
        if pj_uno[5].lower() == "luz":
            for pj_dos in lista:
                if pj_dos[5].lower() == "oscuridad":
                    datos = (pj_uno[3], pj_uno[5], pj_dos[3], pj_dos[5])
                    lista_dd.append(datos)
        if pj_uno[5].lower() == "oscuridad":
            for pj_dos in lista:
                if pj_dos[5].lower() == "agua":
                    datos = (pj_uno[3], pj_uno[5], pj_dos[3], pj_dos[5])
                    lista_dd.append(datos)
        if pj_uno[5].lower() == "agua":
            for pj_dos in lista:
                if pj_dos[5].lower() == "fuego":
                    datos = (pj_uno[3], pj_uno[5], pj_dos[3], pj_dos[5])
                    lista_dd.append(datos)
        if pj_uno[5].lower() == "fuego":
            for pj_dos in lista:
                if pj_dos[5].lower() == "natural":
                    datos = (pj_uno[3], pj_uno[5], pj_dos[3], pj_dos[5])
                    lista_dd.append(datos)
        if pj_uno[5].lower() == "natural":
            for pj_dos in lista:
                if pj_dos[5].lower() == "tierra":
                    datos = (pj_uno[3], pj_uno[5], pj_dos[3], pj_dos[5])
                    lista_dd.append(datos)
        if pj_uno[5].lower() == "tierra":
            for pj_dos in lista:
                if pj_dos[5].lower() == "luz":
                    datos = (pj_uno[3], pj_uno[5], pj_dos[3], pj_dos[5])
                    lista_dd.append(datos)
    return lista_dd

def mata(pj_uno, pj_dos, lista_dd):           #descienden
    # quienes tienen menos puntos
    ataque_uno = pj_uno[1]
    for pj in lista_dd:
        if pj_uno[3] == pj[0] and pj_dos[3] == pj[2]:
            ataque_uno = ataque_uno * 2
    if ataque_uno > pj_dos[2]:
        ataque_uno = ataque_uno - pj_dos[2]
    else:
        ataque_uno = 0
        pj_dos_vida = pj_dos[0] - ataque_uno
    if pj_dos_vida <= 0:
        print(pj_uno[3], "mató a", pj_dos[3])
    else:
        print(pj_dos[3], "sobrevivió al ataque de", pj_uno[3], "con", pj_dos_vida, "de vida")
    ataque_dos = pj_dos[1]
    for pj in lista_dd:
        if pj_dos[3] == pj[0] and pj_uno[3] == pj[2]:
            ataque_dos = ataque_dos * 2
    if ataque_dos > pj_uno[2]:
        ataque_dos = ataque_dos - pj_uno[2]
    else:
        ataque_dos = 0
        pj_uno_vida = pj_uno[0] - ataque_dos
    if pj_uno_vida <= 0:
        print(pj_dos[3], "mató a", pj_uno[3])
    else:
        print(pj_uno[3], "sobrevivió al ataque de", pj_dos[3], "con", pj_uno_vida,"de vida")
        
def aldea(lista):                    #Puntaje
            #puntos por equipos. es un if, que decide por cada gol, etc que tienen los equipos y retorna un puntaje.    
    lista_nueva = lista
    indice = 0
    for pj_uno in lista_nueva:
        mismas_aldeas = []
        for pj_dos in lista_nueva:
            if pj_uno[4] == pj_dos[4] and pj_uno[5] == pj_dos[5] and pj_uno[3] != pj_dos[3]:
                mismas_aldeas.append(pj_dos)
                lista_nueva.remove(pj_dos)
    if mismas_aldeas != []:
        indice = indice + 1
        mismas_aldeas.append(pj_uno)
        print("los siguientes personajes comparten aldeas entre sí")
        print(mismas_aldeas)
    if indice == 0:
        print("ningún personaje comparte aldea con otro")
        
def menu(lista):
    print("presione: 1 - Para saber qué personajes le hacen el doble de daño a otro")
    print("presione: 2 - Para saber si un personaje mata a otro o sobrevive al ataque")
    print("presione: 3 - Para saber qué personajes comparten aldea entre sí")
    print("presione: 0 - Para salir del menú")
    opcion = int(input("elija una opción: "))
    while opcion != 0:
        while opcion != 1 and opcion != 2 and opcion != 3:
            print("elija una opción correcta")
            opcion = int(input("elija una opción: "))
        if opcion == 1:
            for pj in dobledaño(lista):
                print(pj[0], "con elemento", pj[1], "le pega doble a", pj[2].lower(), "con elemento", pj[3].lower())
        if opcion == 2:
            lista_dd = dobledaño(lista)
            print("Existen", len(lista), "personajes, elija dos para poder comparar")
            print("Por ejemplo, puede comparar el personaje número '1' con el personaje número '3', si es que es encuentra dentro del rango")
            pj_uno = int(input("escoja un personaje: "))
            pj_dos = int(input("escoja otro personaje: "))
            mata(lista[pj_uno - 1], lista[pj_dos - 1], lista_dd)
        if opcion == 3:
            aldea(lista)
        opcion = int(input("elija una opción: "))

lista = personajes()
menu(lista)


