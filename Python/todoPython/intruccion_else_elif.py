#uso de else
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

#uso de elif
a = 93
b = 27
if a >= b:
    print ("a es mayor o igual que b")
elif a == b:
    print("a es igual a b")

#uso de if elif else
a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")

#logica combinada
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")