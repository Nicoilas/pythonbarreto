class compañia:
    def __init__(self,titulo,unidades,precio):
        self.__titulo=titulo
        self.__unidades=unidades
        self.__precio=precio

    def gettitulo(self,titulo):
        self.__titulo = titulo
        return self.__titulo

    def settitulo(self):
        self.__titulo

    def getunidades(self,unidades):
        self.__unidades = unidades
        return self.__unidades

    def setunidades(self):
        self.__unidades

    def getprecio(self,precio):
        self.__precio = precio
        return self.__precio

    def setprecio(self):
        self.__precio

