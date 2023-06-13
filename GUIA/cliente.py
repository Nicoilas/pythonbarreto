class cliente:
    def __init__(self, nombre,documento):
        self.__nombre=nombre
        self.__documento=documento

    def getnombre(self, nombre):
        self.__nombre = nombre
        return self.__nombre

    def setnombre(self):
        self.__nombre

    def getdocumento(self, documento):
        self.__documento = documento
        return self.__documento

    def setdocumento(self,documento):
        self.__documento=documento
        