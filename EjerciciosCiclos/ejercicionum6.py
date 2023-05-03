maximo = 0

while True:
    numero = int(input("Introduce un número positivo: "))
    if numero < 0:
        break
    if numero > maximo:
        maximo = numero

print("El máximo de los números introducidos es:", maximo)

