n=int(input("cantidad de participantes: "))
print("colombia-->opcion.1")
print("mexico-->opcion.2")
cont=0
contador=0 
for i in range(1, n+1) :

 voto=int(input(f"asistente numero{i}: "))
 while (voto <1 or voto>2):
    print("opcion no valida")
    voto=int(input(f"asistente numero{i}: "))
 if voto==1:
    cont=cont+1
 if voto==2:
    contador+=1
print("votos para colombia son",cont)  
print("votos para mexico son",contador)          
  