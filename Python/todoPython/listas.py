planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("el primer planeta es: ", planetas[0])
print("el segundo planeta es: ", planetas[1])
print("el tercer planeta es: ", planetas[2])

# Salida
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth


#Dado que todos los índices empiezan por 0, [1] es el segundo elemento, [2] es el tercero, etc.


#Cambiar o modificar valores de la lista mediante un indice:

planetas[3] = "planeta rojo"

print("marte tambien es llamado", planetas[3])


#longitud de una lista

numeros_de_planetas = len(planetas)
print("hay", numeros_de_planetas, " planetas en el sistema solar.")

#metodo .pop() elimina el ultimo elemento de la lista
planetas.pop()  # Goodbye, Pluto
numeros_de_planetas = len(planetas)
print("Ahora hay", numeros_de_planetas, "planetas en el sistema solar")

#devuelve el indice de ese elemento, jupiter es el 4
jupiter_index = planetas.index("Jupiter")
print("Jupiter es el", jupiter_index + 1, "planeta cercano al sol")
#Dado que la indexación comienza por 0, debe agregar 1 para mostrar el número adecuado.