import os
def crear_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' ya existe.")
        with open(nombre_archivo, 'r') as file:
            num_lineas = sum(1 for line in file)
        print(f"El archivo contiene {num_lineas} líneas.")
    else:
        with open(nombre_archivo, 'w'):
            print(f"El archivo '{nombre_archivo}' se ha creado.")

def guardar_datos_personales(nombre_archivo):
    print("Ingrese sus datos personales.")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    direccion = input("Dirección: ")

    with open(nombre_archivo, 'w') as file:
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Edad: {edad}\n")
        file.write(f"Dirección: {direccion}\n")

    print(f"Los datos personales se han guardado en el archivo '{nombre_archivo}'.")

def contar_caracteres(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.")
    else:
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
            num_caracteres = len(contenido)
        print(f"El archivo contiene {num_caracteres} caracteres.")

if __name__ == "__main__":
    archivo_nombre = "datos_personales.txt"

    crear_archivo(archivo_nombre)

    guardar_datos_personales(archivo_nombre)
  
    contar_caracteres(archivo_nombre)