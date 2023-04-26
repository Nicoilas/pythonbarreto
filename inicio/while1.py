# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1
cont=0
sum=0
menor=1000000
mayor=0                                                              #cuando el usuario quiere terminar con el siclo solo tiene que darle al 0 y asi acabara el ciclo del programa
                                                                     #cont se utilza para hacer un contador de numeros para la variable y constantes
                                                                     #y con el print se imprimen las variables que esten seleccionadas o las que cumplen con la funciprint
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1
    sum=sum+num
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num

print(f'fueron ingresados {cont-1} numeros')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')












                                                  