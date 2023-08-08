class Alumno:
    def __init__(self, numero_documento, puntaje, fecha_nacimiento, id_icfes):
        self.__numero_documento = numero_documento
        self.__puntaje = puntaje
        self.__fecha_nacimiento = fecha_nacimiento
        self.__id_icfes = id_icfes

    def verDatos(self):
        return f"{self.__numero_documento} {self.__puntaje} {self.__fecha_nacimiento} {self.__id_icfes}"

    @property
    def numero_documento(self):
        return self.__numero_documento

    @property
    def puntaje(self):
        return self.__puntaje

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @property
    def id_icfes(self):
        return self.__id_icfes
