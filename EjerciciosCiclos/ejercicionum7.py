maximo = int(input("Introduce el valor máximo: "))
suma = 0
n = 1

while suma <= maximo:
    suma += n
    n += 1

print("El número más pequeño de la serie de los naturales que debemos sumar para superar el valor máximo es:", n-1)
