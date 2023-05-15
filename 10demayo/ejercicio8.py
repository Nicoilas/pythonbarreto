import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def imprimir_arreglo(arreglo):
    print(arreglo)

def calcular_suma_pares(arreglo):
    suma_pares = 0
    for numero in arreglo:
        if numero % 2 == 0:
            suma_pares += numero
    return suma_pares

def calcular_promedio_impares(arreglo):
    impares = [numero for numero in arreglo if numero % 2 != 0]
    if impares:
        promedio_impares = sum(impares) / len(impares)
        return promedio_impares
    else:
        return None

n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = generar_arreglo(n)
print("Arreglo generado:")
imprimir_arreglo(arreglo)
suma_pares = calcular_suma_pares(arreglo)
promedio_impares = calcular_promedio_impares(arreglo)
print("Suma de los números pares:", suma_pares)
if promedio_impares is not None:
    print("Promedio de los números impares:", promedio_impares)
else:
    print("No se encontraron números impares en el arreglo.")
