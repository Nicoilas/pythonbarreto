try:
    archivos=open('archivos/himno.txt','r',encoding='utd-8')
    cont=0
    for linea in archivos:
        print(f"{cont}''''{archivos}")
        cont+=1
except IOError as e:
    print(e,'......')