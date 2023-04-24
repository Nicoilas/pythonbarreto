n=int(input("ingrese la cantidad de numeros naturales: "))
while n<=0 :
    print("el numero debe ser posotivo")
    n=int(input("ingrese la cantidad de numeros naturales: "))

    suma=0
    for i in range(1,n+1):
        elevar_cuadrado=i*i
        suma= suma+ elevar_cuadrado
        print ("La suma de los n numeros naturales es: ",suma)
        