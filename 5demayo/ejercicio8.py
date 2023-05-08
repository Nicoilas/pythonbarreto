import random
cont=0
numero= [random.randint(2,15) for _ in range(10)]
num=0
pares = [num for num in numero if num % 2 == 0] 
suma_pares = sum(pares) 
impares = [num for num in numero if num % 2 != 0]
promedio_impares = sum(impares) / len(impares) 

print("Números aleatorios:", numero)
print("Números pares:", pares)
print("Suma de los números pares:", suma_pares)
print("Números impares:", impares)
print("Promedio de los números impares:", promedio_impares)