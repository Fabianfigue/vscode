pagos = []

fecha = input("fech formato dd/mm/aa")
while fecha != '-1':
    n_cliente = int(input("ncliente"))
    precio = float(input("precio"))
    detalle = str(input("detalle"))
    pagos.append([n_cliente, precio, detalle, fecha])
    fecha = str(input("fech formato dd/mm/aa"))
    
    
print(pagos)
    