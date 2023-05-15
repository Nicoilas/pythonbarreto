import random

def generar_arreglo(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(0, 100))
    return lista

def imprimir_arreglo(lista):
    print(lista)

def calcular_promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio

def comparar_con_promedio(lista):
    promedio = calcular_promedio(lista)
    for elemento in lista:
        if elemento > promedio:
            print(elemento, "está por encima del promedio.")
        elif elemento < promedio:
            print(elemento, "está por debajo del promedio.")
        else:
            print(elemento, "es igual al promedio.")

n = int(input("Ingrese el tamaño de la lista: "))
lista = generar_arreglo(n)
print("Arreglo generado:")
imprimir_arreglo(lista)
print("Promedio del arreglo:", calcular_promedio(lista))
print("Comparación con el promedio:")
comparar_con_promedio(lista)
