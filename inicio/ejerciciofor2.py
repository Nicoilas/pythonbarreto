n = int(input("Ingrese un número positivo: "))
count = 0

if n > 0:
    for i in range(n+1):
        if i % n == 0:
            count += 1

    print(f"Hay {count} múltiplos de {n} en la serie del 0 al {n}.")
else:
    print("El número ingresado no es válido. Por favor, ingrese un número positivo.")
-8