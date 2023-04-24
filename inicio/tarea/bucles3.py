n=int(input("ingrese la cantidad: "))
i=1
prducto=1
impar=1
par=1
for i in range(n):
    num=int(input("ingrese el numero; "))
    prducto=prducto*num
    if num% 2 ==0:
        impar=impar*num
    else:
        par=par*num

print("el producto de todos los numeros es: ",prducto)
print("el producto de los numeros pares; ",par)
print("el producto de los numeros impares: ",impar)
