nom = str(input("Ingrese un nombre: "))
nombres = 0
while nom != "zzz":
    if nom[0] == "a" or nom[0] == "A":
        nombres = nombres + 1
        print(nombres)
    nom = str(input("Ingrese un nombre: "))
