class persona:
    def __init__(self,nombre,documento,):
        self.__nombre__=nombre
        self.__documento__=documento
        self.__cursos__=[]
    def getnombre(self):
        return self.__nombre__    
    def setnombre(self,nombre):
        self.__nombre__=nombre
    def getdatos(self):
        return self.__documento__ 
    def setdatos(self,documento):
        self.__documento__=documento
    def getDatos(self):
        return f'{self.__nombre__} , {self.__documento__}'
    def setcursos(self,cursos):
        self.__cursos__.append=cursos
    def getcursos(self,):
        return self.__cursos__    
      
p=persona('Nicolas',54924)
print(p.getnombre())
p.setnombre('Juan')
print(p.getnombre())

print(p.getDatos())
p.getDatos()

q=persona('Salome',54156)
print(q.getnombre())
q.setnombre('Sheynna')
print(q.getnombre)    

print(q.getDatos())
q.getDatos()

print(q.getcursos)
      
        