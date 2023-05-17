


import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
def sumalista(lista): 
    
    sum=0
    for i in lista:
        sum+=i
        total=sum
    return total

l1=llenarLista(10,50)    
l2=llenarLista(10,50)  
print(l1)
print(l2)
print()
print("la suma es", sum(l1))
print("la suma es", sum(l2))

def sumaMayor(l1,l2):
    totalgen=0
    if sumalista(l1)<sumalista(l2):
        totalgen=sumalista(l2)
    else:
        sumalista(l1)>sumalista(l2)
        totalgen=sumalista(l1)
    return totalgen    

print(sumaMayor(l1,l2))    


