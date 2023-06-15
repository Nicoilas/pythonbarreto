from persona import *

class cordinador (persona):
    def __init__(self,id, codigo, nombre,direccion, fecha_ingreso, dir_oficina,nombre_cordinador, telefono):
        super().__init__(id,codigo, nombre,direccion,telefono)
        self.__fecha_ingreso__=fecha_ingreso
        self.__dir_oficina__=dir_oficina
        self.__nombre__=nombre
        self.__nombre_cordinador__=nombre_cordinador
        
    def setid (self):
        self.id__
    def getid(self):
        return self.id__
    def setcodigo(self):
        self.__codigo__
    def getcodigo(self):
        return self.__codigo__            
    def setfecha_ingreso(self):
        self.__fecha_ingreso__
    def getfecha_ingreso(self):
        return self.__fecha_ingreso__
    def setdir_oficina(self):
        self.__dir_oficina__
    def getdir_oficina(self):
        return self.__dir_oficina__
    def setnombre_cordinador(self):
        self.__nombre_cordinador__
    def getnombre_cordinador(self):
        return self.__nombre_cordinador__    
    def get_informacion(self):
        return (self.__dict__)    