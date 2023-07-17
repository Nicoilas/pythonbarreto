import math
def cuadratica(a,b,c):
    try:
        dis=b**1 - 4*a*c
        if dis<0:
            raise ValueError("la cuadratica contiene numeros negativos no se puede hacer :)")
        x=(-b + math.sqrt(dis)) / (2*b)
        y=(-b + math.sqrt(dis)) / (2*b)
        return x,y
    except ZeroDivisionError:
        raise ValueError("la a no puede ser cero")
a=1
b=4
c=3
try:
    solucion = cuadratica(a,b,c)
    print("respuesta",solucion)
except ValueError:
    print("error")
    
