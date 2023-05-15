import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def imprimir_arreglo(arreglo):
    print(arreglo)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(arreglo):
    primos = []
    contador = 0
    for numero in arreglo:
        if es_primo(numero):
            contador += 1
            primos.append(numero)
    return contador, primos

n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = generar_arreglo(n)
print("Arreglo generado:")
imprimir_arreglo(arreglo)
cantidad_primos, primos = contar_primos(arreglo)
print("Cantidad de números primos:", cantidad_primos)
print("Números primos encontrados:", primos)
