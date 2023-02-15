def lista(l):
  nom = input("Ingrese nombre del alumno/a o ZZZ para finalizar carga")
  while nom != "ZZZ":
    ape = input("Ingrese apellido del alumno/a")
    leg = int(input("Ingrese legajo del alumno/a"))
    ln = []
    ntas = float(input("Ingrese nota del alumno/a o 888 para finalizar carga de notas"))
    while ntas != 888 :
      ln.append(ntas)
      ntas = float(input("Ingrese nota del alumno/a o 888 para finalizar carga de notas"))
    l.append([nom, ape, leg, ln]) 
    nom = input("Ingrese nombre del alumno/a o ZZZ para finalizar carga")
  return l

print(lista([]))