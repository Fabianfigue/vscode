def sumaPrimUlt(lis):
    suma = (lis[0]) + (lis[2])
    return ("el resultado: " + str(suma))

def promedioPrimUlt(lis):
    promedio = (lis[0] + lis[2]) / 2
    return ("El resultado: " + str(promedio))

primer_num = int(input("Ingre: "))
segundo_num = int(input("Ingre: "))
tercer_num = int(input("ingres: "))

lista = [primer_num, segundo_num, tercer_num]
print(lista)
print(sumaPrimUlt(lista))
print(promedioPrimUlt(lista))