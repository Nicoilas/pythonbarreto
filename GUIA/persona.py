class persona:
    def __init__ (self, alias, correo,telefono):
        self.__alias = alias
        self.__correo = correo
        self.__telefono = telefono

    def getalias(self, alias):
        self.__alias = alias
        return self.__alias

    def setalias(self):
        self.__alias

    def getcorreo(self, correo):
        self.__correo = correo
        return self.__correo

    def setcorreo(self):
        self.__correo

    def gettelefono(self, telefono):
        self.__telefono = telefono
        return self.__telefono

    def settelefono(self):
        self.__telefono