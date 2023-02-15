from io import open

def leerArchivo(): #funcion que retorna una lista con sublistas.
    #lee la cantidad de lineas que tiene mi archivo
    archivo_texto=open("archivo.txt","r")#abrimos el archivo en modo read, para su lectura por pantalla
    for cont, linea in enumerate(archivo_texto): #enumerate: funcion para contar lineas de un archivo                        
        continue
    archivo_texto.close() #siempre que se llama al archivo hay que cerrarlo

    #leer linea del archivo
    archivo_texto=open("archivo.txt","r")
    lista = []
    for equipo in range(0, cont+1):
         texto = archivo_texto.readlines(equipo+1) 
         #funcion que lee linea x linea
         #+1 para que imprima linea x linea y no todo el archivo
         lista.append(texto)
    archivo_texto.close()
    del lista[0] #borra cabecera de guia
    return lista

    
    
listaEquipos = leerArchivo()
print(listaEquipos)
