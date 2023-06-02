class persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getdocumento(self):
        return self.__documento
    def setdocumento(self,documento):
        self.__documento=documento
    def getDatos(self):
        return f'{self.__nombre} , {self.__documento}'
  
            
        
p=persona('Ana',123)
print(p.getNombre())
p.setNombre('jary')
print(p.getNombre())

q=persona('pedro',321)
print(q.getNombre())
q.setNombre('Emiliano')
print(q.getNombre())

print(q.getDatos())
q.getDatos()


            