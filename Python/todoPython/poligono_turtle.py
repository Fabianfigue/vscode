import turtle

def poligono(t, longitud, n):
    t = turtle.Turtle()
    for i in range(20):
        t.fd(longitud)
        t.lt(n)
    print(t)
    

g = 18.2
n = str('bob')
valor = 18.2
l = valor
bob = poligono(n, l, g)



turtle.mainloop()

def circulo(t, r):
    t = turtle.Turtle()
    for i in range(r):
        t.fd(poligono)

radio = 6
perimetro = 2 * 3,14 * radio
t = str('fab')
fab = circulo(t, radio)


