int(input("ingrese un numro"))
def euclides(m, n):
    
    if n == 0:
        return m
    
   
    else:
        return euclides(n, m % n)
    
print(euclides(12, 18)) 