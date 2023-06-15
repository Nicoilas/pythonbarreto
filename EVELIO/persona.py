class persona:
    def __init__(self,id,codigo,nombre,direccion,telefono):
        self.__id__=id
        self.__codigo__=codigo
        self.__nombre__=nombre
        self.__direccion__=direccion
        self.__telefono__=telefono
    def setid(self):
        self.__id__
    def getid(self):
        return self.__id__
    def setcodigo(self):
        self.__codigo__
    def getcodigo(self):
        return self.__codigo__
    def setnombre(self):
        self.__nombre__
    def getnombre(self):
        return self.__nombre__
    def setdireccion(self,direccion ):
        self.__direccion__=direccion
    def getdireccion(self):
        return self.__direccion__
    def settelefono(self):
        self.__telefono__
    def gettelefono(self):
        return self.__telefono__         
    def get_informacion(self):
        return (self.__dict__) 
    # def ver_informacion(self):
    #     return f"{self.__id__} {self.__codigo__} {self.__nombre__} {self.__direccion__}{self.__telefono__}"





#p=persona(1,34,'Nicolas','cr 14 c', 915756156)
#print(p.ver_informacion())
# q=persona(1,32,'Salome','cr 89 c', 584514)
# print(q.ver_informacion())
# d=persona(7,39,'Sheynna','cr 89 c', 54694)
# print(d.ver_informacion())

        
        
            
    