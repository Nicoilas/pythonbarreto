from random import randint


num1 = randint(1, 100)
num2 = randint(1, 100)


while num1 == num2:
    num2 = randint(1, 100)


print("Los números generados son:", num1, "y", num2)


mayor = max(num1, num2)
menor = min(num1, num2)


resultado = mayor - menor
print("El resultado de la primera resta es:", resultado)


if resultado > 0:
    resultado = resultado - menor
    print("El resultado de la segunda resta es:", resultado)
else:
    print("El resultado de la primera resta es cero, no se puede restar más.")
print("El resultado final es:", resultado)