#Escribir un programa que muestre la tabla de los códigos ASCII. Los códigos
#ASCII van de 0 a 255
for i in range(0, 256):
    print(str(i) + ' = ' + chr(i))