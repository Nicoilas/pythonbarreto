def es_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    else:
        return False
print(es_perfecto(6))  
print(es_perfecto(28))  
print(es_perfecto(10))  
