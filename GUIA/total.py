class Cliente:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento


class Compania:
    def __init__(self, titulo, unidades, precio):
        self.__titulo = titulo
        self.__unidades = unidades
        self.__precio = precio

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_unidades(self):
        return self.__unidades

    def set_unidades(self, unidades):
        self.__unidades = unidades

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


class Persona:
    def __init__(self, alias, correo, telefono):
        self.__alias = alias
        self.__correo = correo
        self.__telefono = telefono

    def get_alias(self):
        return self.__alias

    def set_alias(self, alias):
        self.__alias = alias

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono


class Producto:
    def __init__(self, proveedor, cliente):
        self.__proveedor = proveedor
        self.__cliente = cliente

    def get_proveedor(self):
        return self.__proveedor

    def set_proveedor(self, proveedor):
        self.__proveedor = proveedor

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente



per = Persona('kakaroto', 'henkidama@gmail.com', 3203169805)
com = Compania('capsula_corp', 10, 200000)
pro = Producto('RR', 'kakaroto')
cli = Cliente('vegeta', 8000)


print(per.get_alias())  
per.set_telefono(123456789)  
print(per.get_telefono())  

print(com.get_titulo())  
com.set_unidades(20)  
print(com.get_unidades())

print(pro.get_proveedor())
pro.set_cliente('goku')  
print(pro.get_cliente())  
print(cli.get_nombre())
cli.set_documento(9000) 
print(cli.get_documento()) 
