import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

l1=llenarLista(5,20)
l2=llenarLista(10,50)
l3=llenarLista(3,1000)
print(l1)
print(l2)
print(l3)
print(sumaLista(l1))
print(sumaLista(l2))
print(sumaLista(l3))
print(promedioLista(l1))
print(promedioLista(l2))
print(promedioLista(l3))

def mayor(lista):
   m=0
   for i in lista:
       if i>m:
        m=i
       return m
print("mayor",mayor(l1))
print("mayor",mayor(l2))
print("mayor",mayor(l3))
   

def menor(lista):
    m=0
    for i in lista:
       if i>m:
         m=i
       return m
print("menor",menor(l1))
print("menor",menor(l2))
print("menor",menor(l3))

def ordenar_ascendente(lista):
   lista.sort()
print("Arreglo ordenado en orden ascendente:")
print(l1)
print(l2)
print(l3)

def ordenar_desendente(lista):
   lista.sort()
print("Arreglo ordenado en orden desendente:")   
print(l1)
print(l2)
print(l3)

import statistics

def calcular_moda(lista):
    try:
        moda = statistics.mode(lista)
        print("La moda del arreglo es:", moda)
        print(l1)
        print(l2)
        print(l3)
    except statistics.StatisticsError as e:
        print("No se puede calcular la moda del arreglo:", e)
        print(l1)
        print(l2)
        print(l3)

def mediana(lista):
    e=0
    for i in lista:
       if i>e:
         e=i
       return e
print("mediana",mediana(l1))
print("mediana",mediana(l2))
print("mediana",mediana(l3))

def buscar_numero(lista):
   b=0
   for i in lista:
      if i>b:
         b=i
      return b  
print("buscar_numero",buscar_numero(l1))
print("buscar_numero",buscar_numero(l2))
print("buscar_numero",buscar_numero(l3))   
   


        
  
   


