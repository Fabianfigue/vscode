def datos_usuario(nombre, apellido):
    saludo = ("hola " + nombre + " " + apellido + " Bienvenidos al sistema")
    return saludo
    
n = input("ingrese su nombre: ")
a = input("ingrese su apellido: ")

nombre_apellido = datos_usuario(n,a)
print (nombre_apellido)
