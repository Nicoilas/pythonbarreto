#x,y=3,5
#cont=1
#while not(x%y==0 or y%x==0):                 #se utilza la variable while cuando la variable que este en el programa comiensa en cero
    #print(f'intento numero {cont}')
    #x=int(input('ingrese numero'))
    #y=int(input('ingrese numero'))
    #cont+=1

#print(f'{x} y {y} son factor')
import random
lista=[]
sum=0
total=0
prod=0
mayor=0
menor=0
moda=0
resta=0
contador=0
raiz=0
cuadrado=0
tam=random.randint(10,11)
print(tam)
for i in range(tam):
    num=random.randrange(5)
    lista.append(num)
    print(lista)

for i in range(len(lista)):
    sum+=lista[i]
    total=sum
    prod=total//len(lista)
    print(f"la suma total{total} ")
    print(f"promedio es {prod}")

for i in lista:
    if i >mayor:
        mayor=i
    if i <menor:
        menor=i
    print(f"el mayor es={mayor}")
    print(f"el menor es={menor}")

for i in lista:
    if tam==i:
     moda=i
    print(f"la moda es={moda}")    

for i in range(tam):
    num = random.randrange(5)
    lista.append(num)

print(lista)

desviacion_estandar = (lista)
print("La desviación estándar de la lista es:", desviacion_estandar)

for i in range(tam):
    num = random.randrange(5)
    lista.append(num)

print(lista)