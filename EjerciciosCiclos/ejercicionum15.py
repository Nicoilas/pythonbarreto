num=int(input("ingrese un numero"))

for i in range (num,0,-1):
    for x in range (1,i,+1):
        print(x,end="")
    print()    