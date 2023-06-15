from persona import *
class instructor(persona):
    def __init__(self,id,codigo,nombre,direccion,telefono,profecion, especialidad, cargo, salario_basico):
        super().__init__(id,codigo,nombre,direccion,telefono)
        self.__profecion__=profecion
        self.__especialidad__=especialidad
        self.__cargo__=cargo
        self.__salario_basico__=salario_basico
    def setprofecion(self):
        self.__profecion__
    def getprofecion(self):
        return self.__profecion__
    def setespecialidad(self):
        self.__especialidad__
    def getespecialidad(self):
        return self.__especialidad__
    def setcargo(self):
        self.__cargo__
    def getcargo(self):
        return self.__cargo__
    def setsalario_basico(self):
        return self.__salario_basico__
    
    def get_informacion(self):
        return (self.__dict__)    
   
   
   
   
   
   
   
    # def ver_informacion(self):
    #     return f'{self.__profecion__} {self.__especialidad__} {self.__cargo__} {self.__salario_basico__}'
#p=instructor('maestro', 'maestria', 'docente', 250000)
#print(p.ver_informacion())
    
                    
    # def ver_informacuion(self):   
    #     return f"{self.profecion__} {self.especialidad__} {self.cargo__} {self.salario_basico__}"
     