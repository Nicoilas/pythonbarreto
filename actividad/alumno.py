#crear un documento y que la respuesta salga en otro archivo
class alumno:
    def __init__(self,numero_documento,puntaje,fecha_nacimiento,id_icfes,):
        self.__numero_documento=numero_documento
        self.__puntaje=puntaje
        self.__fecha_nacimiento=fecha_nacimiento
        self.__id_icfes=id_icfes
    def verDatos(self):
        return f"{self.__numero_documento}{self.__puntaje}{self.__fecha_nacimiento}{self.__id_icfes}"
    def getDatos(self):
        return self.__numero_documento
    def getDatos(self):
        return self.__puntaje
    def getDatos(self):
        return self.__fecha_nacimiento
    def getDatos(self):
        return self.__id_icfes