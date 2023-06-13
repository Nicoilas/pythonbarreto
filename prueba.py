lista=[]

while lista == -0:
    l=input(' :')
    while l not in lista:
        lista.append(l)
    if l == 'fin':
        break



print(lista)