import random
import math
lista=[]
tam=random.randint(2,15)
cont=0
numero=0
num=0

numeros = [random.randint(2, 15) for i in range(10)]
factoriales = []
for numero in numeros:
    factorial = math.factorial(numero)
    factoriales.append(factorial)

print("Números aleatorios: ", numeros)
print("Factoriales: ", factoriales)

