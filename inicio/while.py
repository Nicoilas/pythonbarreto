num=1
cont=0
sum =0
prod=2
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1
    sum = sum+cont
    
print(f'fueron ingresados {cont+0} numeros')
print(f"suma todad de {sum} numeros ")

prod= sum/cont
print(f"el promedio de {prod} numeros")    


