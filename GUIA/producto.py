class producto:
    def __init__(self, proveedor,cliente):
        self.__proveedor = proveedor
        self.__cliente = cliente
    def getproveedor(self,proveedor):
        self.__proveedor=proveedor
        return self.__proveedor
    def setproveedor(self):
        self.__proveedor
    
    def getcliente(self,cliente):
        self.__cliente=cliente
        return self.__cliente
    
    def setcliente(self):
        self.__cliente