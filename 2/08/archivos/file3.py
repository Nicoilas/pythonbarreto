try:
    stream=open('file/himno.txt','r',encoding='utd-8')
    cont=1
    linea=stream.readline()
    c=1
    while linea!="":
        print(f"{c}{linea}")
        linea=stream.readline()
        c+1
except IOError as e:
    print(e,'.....')