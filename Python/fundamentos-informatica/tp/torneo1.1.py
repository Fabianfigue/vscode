# Tema: Torneo de futbol
# Datos a cargar: equipos, cantidad partidos ganados, cantidad partidos perdidos, empates, goles a favor, goles en contra.
# Funciones:
# 1-	Equipos (carga equipos con sus datos y retorna una lista)
# 2-	Ganador por mayoría de goles (retorna el equipo que mas goles hizo en el torneo)
# 3-	Puntaje (Calcula y retorna el puntaje de los equipos, según los datos cargados)
# 4-	Quien desciende (retorna el equipo que menos puntos tiene en el torneo)
# 5-	Desempate(Carga dos equipos y los lleva a un desempate por goles, y goles en contra y retorna ganador)


#importar modulo io (open, para abrir archivo y utilizarlo)
from io import open
#Funciones:
#Crea una lista del archivo importado que voy a utilizar mas adelante
def listaDeArchivo():
    archivo_texto=open("archivo.txt","r")               #lee la cantidad de lineas que tiene mi archivo
    for cont, linea in enumerate(archivo_texto):        #enumerate: funcion para contar lineas de un archivo
        continue                                        #uso de continue para que el for siga ejecutando hasta que enumerate termine
    archivo_texto.close()                               #.close() cierra archivo 
    
    #leer linea del archivo
    archivo_texto=open("archivo.txt","r")
    lista = []                                          #creo una lista para guardar los datos de archivo en formato lista
    for equipo in range(0, cont+1):
        texto = archivo_texto.readlines(equipo+1)       #.readlines()   funcion que lee linea x linea
                                                        #+1 para que imprima linea x linea y no todo el archivo
        texto = texto[0].split(',')                     #metodo split para separar los elementos por cada coma que encuentre en el archivo
        lista.append(texto)
    archivo_texto.close()
    del lista[0]                                        #del lista[0] borra cabecera de guia
    return lista

#mostrarEquipos(): retorna la leyenda del inicio del programa que nos muestra los equipos que tiene archivo cargados.
def mostrarEquipos():
    archivo_texto=open("archivo.txt","r")
    texto = archivo_texto.read()
    archivo_texto.close()
    return texto

#Equipos (carga equipos con sus datos y retorna una lista)
def equipos():
    lista = []
    indiceEquipos = 0                                                                           #contador para que en linea 53 agrege el equipo en una nueva linea
    nombre = ("\n") + input("Ingrese el nombre del equipo a cargar: ")+ (",")                   #\n y "," son utilizados para que se guarden los datos correctamente dentro de archivo
    while nombre != "\nfin,":
        partidos_ganados = input("Ingrese la cantidad de partidos ganados: ") + (",")
        partidos_perdidos = input("Ingrese la cantidad de partidos perdidos: ")+ (",")
        empates = input("Ingrese la cantidad de empates: ")+ (",")
        goles_aFavor = input("Ingrese los goles a favor: ")+ (",")
        goles_enContra = input("Ingrese los goles en contra: ")
        lista.append([nombre, partidos_ganados, partidos_perdidos, empates, goles_aFavor, goles_enContra]) #agregar nuevo equipo a lista de memoria
        archivo_texto=open("archivo.txt","a")                                                   #abro archivo en modo append. para modificarlo
        texto = archivo_texto.writelines(lista[indiceEquipos])
        archivo_texto.close()
        indiceEquipos += 1
        nombre = ("\n") + input("Ingrese nombre del equipo o la palabra 'fin' para terminar de cargar datos. ")+ (",")
        
    return texto


#Ganador por mayoría de goles (retorna el equipo que mas goles hizo en el torneo)
def ganador_por_goles(list):
    goles = 0
    ganador = ""
    for i in list:                                  #recorro la lista retornada por archivoDeArchivo()
        cuenta = int(i[4]) + int(i[5])              #suma los goles_aFavor y goles_enContra
        if cuenta > goles:                          #si la cuenta es mayor a los goles que va contando. los guarda y guarda al actual ganador.
            goles = cuenta
            ganador = i[0]
    return "el equipo ganador por goles es: " + ganador + " Con " + str(goles) + " goles en total"


#Reglas puntaje:
    #partidos ganados(5 puntos)
    #partidos perdidos(-0.5 puntos)
    #empates(2 puntos)
    #goles a favor(3 puntos)
    #goles en contra(-0.5 puntos)
#Puntaje (Calcula y retorna el puntaje de los equipos, según los datos cargados)
def puntaje(list): 
    for i in list:
        ganados = int(i[1]) * 5
        perdidos = int(i[2]) * (-0.5)
        empates = int(i[3]) * 2
        goles_aFavor = int(i[4]) * 3
        goles_enContra = int(i[5]) * (-0.5)
        cuenta = ganados + perdidos + empates + goles_aFavor + goles_enContra
        equipo = i[0]
        print("El puntaje del equipo " + equipo + " es: " + str(cuenta))
    return


#Quien desciende (retorna el equipo que menos puntos tiene en el torneo)
def desciende(list): 
    desciende = ""
    cont = 10000000000                          #utilice un numero muy alto para que siempre la cuenta al iniciar el for se guarde y pise esta variable.
    for i in list:
        ganados = int(i[1]) * 5
        perdidos = int(i[2]) * (-0.5)
        empates = int(i[3]) * 2
        goles_aFavor = int(i[4]) * 3
        goles_enContra = int(i[5]) * (-0.5)
        cuenta = ganados + perdidos + empates + goles_aFavor + goles_enContra
        if cuenta < cont:
            cont = cuenta
            desciende = i[0]
    return "el equipo que desciende es: " + desciende + " Por minoria de puntos."

#desempata equipos ingresados por el usuario de forma manual(2 equipos solamente)
#en caso de que no haya un desempate en primer if. entra a otro while que desempata por otros parametros.
def desempate():
    equipos = []
    cont = 1
    while cont <= 2:
        nombres = input("Ingrese el nombre del equipo: ")
        goles = int(input("ingrese cantidad de goles: "))
        goles_en_contra = int(input("Ingrese cantidad de goles en contra: "))
        equipos.append([nombres, goles, goles_en_contra])
        cont += 1
    if (equipos[0][1] + equipos[0][2]) > (equipos[1][1] + equipos[1][2]):
        print("ganador: " + str(equipos[0][0]))
    elif (equipos[1][1] + equipos[1][2]) > (equipos[0][1] + equipos[0][2]):
        print( "ganador: " + str(equipos[1][0]))
    elif (equipos[0][1] + equipos[0][2]) == (equipos[1][1] + equipos[1][2]):
        print("La cantidad de goles es la misma, se procedera a decidir por quien gano mas partidos, restando los partidos perdidos")
        list = []
        cont = 1
        indiceEquipos = 0
        while cont < 3:
            partidos = int(input("ingrese cantidad de partidos ganados de " + equipos[indiceEquipos][0]+ ": "))
            partidos_perdidos = int(input("Ingrese cantidad de partidos perdidos de " + equipos[indiceEquipos][0]+ ": "))
            list.append([nombres, partidos, partidos_perdidos])
            cont += 1
            indiceEquipos += 1
        if (list[0][1] - list[0][2]) > (list[1][1] - list[1][2]):
            print("ganador: " + str(list[0][0]))
        elif (list[1][1] - list[1][2]) > (list[0][1] - list[0][2]):
            print( "ganador: " + str(list[1][0]))
        else:
            print("Imposible desempatar")

#Programa principal:
print("--------------------------menu-----------------------------")
print("------1-Mostrar equipos pre-cargados \n------2-salir")
opcion1 = int(input("###Ingrese una opcion: "))
listaEquipo = listaDeArchivo()
while opcion1 != 2:
    if opcion1 == 1:
        print("-----------------------------------------------------------")
        print(mostrarEquipos())
        print("-----------------------------------------------------------\n-----------------------------------------------------------")
        print("--------------------------menu-----------------------------\n------1-Ganador por goles \n------2-Puntaje de los equipos \n------3-Quien desciende \n------4-Hacer un desempate\n------5-Cargar nuevo equipo \n------6-Salir")
        opcion2 = int(input("###Ingrese una opcion: "))
        
        while opcion2 != 6:
            if opcion2 == 1:
                print(ganador_por_goles(listaEquipo))
            elif opcion2 == 2:
                puntaje(listaEquipo)
            elif opcion2 == 3:
                print(desciende(listaEquipo))
            elif opcion2 == 4:
                print("-------------------Reglas de desempate---------------------")
                print("------Tenes que ingresar dos equipos a desempatar----------")
                print("##En caso de no encontrar diferencias\n##En ninguna de las dos instancias de prueba\n##Se considera que no se pueden desempatar.\n##Los partidos perdidos en la segunda instancia de desempate. Restan el total de los partidos ganados. ")
                desempate()
            elif opcion2 == 5:
                equipos()
            else:
                print("###Ha ingresado mal, vuelva a intentar: ")
            print("--------------------------menu-----------------------------\n------1-Ganador por goles \n------2-Puntaje de los equipos \n------3-Quien desciende \n------4-Hacer un desempate\n------5-Cargar nuevo equipo \n------6-Salir")
            opcion2 = int(input("###Ingrese una opcion: "))
    else:
        print("###Ha ingresado mal, vuelva a intentar")
    print("------1-Mostrar equipos pre-cargados \n------2-salir")
    opcion1 = int(input("###Ingrese una opcion: "))
#fin del programa. en este punto esta fuera del while y solo es mostrado si el usuario preciona el 2 para salir en el primer menu.
print("######## Usted ha salido del programa! ###########")