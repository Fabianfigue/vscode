new_planet_input = ''
planets = []

while new_planet_input.lower() != "listo":
    if new_planet_input:
      planets.append(new_planet_input)
    new_planet_input = input("Enter a new planet, or done if listo")

print(planets)