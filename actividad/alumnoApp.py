from alumno import Alumno
import csv

with open('icfes.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    alumnos = []
    for row in csvReader:
        objeto = Alumno(row[0], row[1], row[2], row[3])
        alumnos.append(objeto)
        print(objeto.verDatos())
        print('numero_documento:', row[0])
        print('puntaje:', row[1])
        print('fecha_nacimiento:', row[2])
        print('id_icfes:', row[3])


with open('output.txt', 'w') as output_file:
    for ap in alumnos:
        output_file.write(f"numero_documento: {ap.numero_documento}\n")
        output_file.write(f"puntaje: {ap.puntaje}\n")
        output_file.write(f"fecha_nacimiento: {ap.fecha_nacimiento}\n")
        output_file.write(f"id_icfes: {ap.id_icfes}\n")
