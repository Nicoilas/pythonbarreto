inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))
cantidad = int(input("Ingrese la cantidad a incrementar o decrementar según el caso: "))


if cantidad > 0:
   
    for i in range(inicio, fin+1, cantidad):
        print(i, end=" ")
else:
    
    for i in range(inicio, fin-1, cantidad):
        print(i, end=" ")