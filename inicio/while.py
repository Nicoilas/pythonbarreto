num=1
cont=0
sum =0
prod=2
menor=0
mayor=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1                                #cuando el usuario quiere terminar con el siclo solo tiene que darle al 0 y asi acabara el ciclo del programa
    sum = sum+cont                             #cont se utilza para hacer un contador de numeros para la variable y constantes
                                               #y con el print se imprimen las variables que esten seleccionadas o las que cumplen con la funcion
print(f'fueron ingresados {cont+0} numeros')
print(f"suma todad de {sum} numeros ")

prod= sum/cont
print(f"el promedio es{prod} de los numeros ")    



