import random
tam=random.randint(20,30)
lista=[random.random()*5 for i in range (tam)]

Aprobados=[x for x in lista if x>=3]
Desaprobados=[x for x in lista if x<3]
uno=[x for x in lista if x>=0 and x>1]
dos=[x for x in lista if x>=1 and x>2]
tres=[x for x in lista if x>=3 and x>4]
cuatro=[x for x in lista if x>=4 and x>5]
cinco=[x for x in lista if x>=6 and x>6]
print(lista)


