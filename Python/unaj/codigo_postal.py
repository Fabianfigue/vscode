#Escriba un programa que solicite nombres de localidades y códigos postales
#al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los
#valores ingresados e imprimirla.


valores = []
local = str(input('ingrese localidad: '))
cod_post = input('ingrese codigo postal: ')


while cod_post != 0:
    valores.append([cod_post, local])

    local = str(input('ingrese localidad: '))
    cod_post = int(input('ingrese codigo postal: '))

print(valores)