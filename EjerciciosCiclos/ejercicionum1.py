num=int(input("ingrese un numero"))
cont=0

for i in range (1,num+1):
    if num % i == 0 :
        print(f"{i}es divisor")
        cont+=1
print(f"el numero {num}tiene {cont}divisores")