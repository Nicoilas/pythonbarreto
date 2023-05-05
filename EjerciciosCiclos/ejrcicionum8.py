n = int(input("Ingrese un número: "))
multiplosde5 = []

for i in range(1, n+1):
    if i % 5 == 0:
        multiplosde5.append(i)

print("Los múltiplos de 5 comprendidos entre 1 y", n, "son:", multiplosde5)
