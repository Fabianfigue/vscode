#Escribir un programa que lea dos números “n” y “m” y determine si n es
#divisible por m, mostrando el siguiente mensaje por pantalla: “El número n es/no es
#divisible por m”. Reemplazar n y m por los números correspondientes.
n = ord("n")
m = ord("m")
if n/m:
    print ("si se dividen")
else:
    print("no se dividen")
n = 110
m = 109

#Desarrollar un programa en el que se ingrese un año de nacimiento e
#indique si la persona es bebé, menor, adolescente, adulto o adulto mayor.
edad = 78
if edad >=0 and edad <=2:
    print("bebe")
elif edad >2 and edad <=12:
    print("menor")
elif edad >12 and edad <=18:
    print("Adolescente")
elif edad >18 and edad <=75:
    print("adulto")
else:
    print("Adulto mayor")

def lados_triangulo(lado1, lado2, lado3):
    if (lado1+lado2>lado3 and lado2+lado3>lado1 and lado1+lado3>lado2):
        return True
    else:
        return False