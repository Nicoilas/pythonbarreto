numero=int(input("ingrese el numero: "))
contador=0
for i in range(1,numero+1):
    if numero%i==0:
        print(i)
        contador=contador+1
        print("la cantidad de divirsores de",numero,"es",contador)
        