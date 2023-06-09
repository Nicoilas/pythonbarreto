class Empleado:
    suma = 0
    contador = 0

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleado.suma += salario
        Empleado.contador += 1

    def getnombre(self):
        return self.nombre

    def setnombre(self, nombre):
        self.nombre = nombre

    def getcargo(self):
        return self.cargo

    def setcargo(self, cargo):
        self.cargo = cargo

    def getsalario(self):
        return self.salario

    def setsalario(self, salario):
        self.salario = salario

    def calcularsalarioporhora(self):
        horas_diarias = 8
        dias_trabajados = 5
        salario_por_hora = self.salario / (horas_diarias * dias_trabajados)
        return salario_por_hora

    def calcularincrementosalario(self, ipc,salariominimo):
        incremento = ipc
        if self.salario == salariominimo:
            incremento += 0.03
        aumento = self.salario * incremento
        return aumento

    def calcularsalarioconhorasextras(self, horas_extras):
        if horas_extras > 2:
            horas_extras = 2
        salario_con_extras = self.salario + (self.salario / 8) * horas_extras
        return salario_con_extras

    classmethod
    def mostrarsumasalarios(cls):
        return cls.suma

    classmethod
    def calcularpromediosalarios(cls):
        promedio = cls.suma / cls.contador
        return promedio

A=Empleado("Juan")
print(A.getnombre())
A.setnombre("Nicolas")   
print(A.getnombre)     