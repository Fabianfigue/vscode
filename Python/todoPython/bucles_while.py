while condition:
    #codigo aqui

user_input = ""

while user_input.lower() != "listo" :
    user_input = input ('Introduzca un nuevo valor, o listo cuando haya terminado')

#Puede usar la cadena recién escrita como lo haría con cualquier otra 
#cadena capturada con input. Si quiere agregarla a una lista, puede usar código similar al
#ejemplo siguiente:

# Crear la variable para la entrada del usuario
user_input = ''
# Crear la lista para almacenar los valores
inputs = []

# El bucle while
while user_input.lower() != 'listo':
    # Comprueba si hay un valor en user_input
    if user_input:
        # Almacenar el valor en la lista
        inputs.append(user_input)
    # Solicitar un nuevo valor
    user_input = input('Introduzca un nuevo valor, o listo cuando haya terminado')