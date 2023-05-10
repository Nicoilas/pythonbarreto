import random
import statistics

calificaciones =[]
for i in range(20, 31):
 calificaciones.append(round(random.uniform(0, 5), 1))

aprobados =[]
reprobados =[]
for calificacion in calificaciones:
    if calificacion >= 3:
        aprobados.append(calificacion)
    else:
        reprobados.append(calificacion)

grupo1 = []
grupo2 = []
grupo3 = []
grupo4 = []
grupo5 = []
for calificacion in calificaciones:
 if calificacion >= 0 and calificacion < 1:
        grupo1.append(calificacion)
 elif calificacion >= 1 and calificacion < 2:
        grupo2.append(calificacion)
 elif calificacion >= 2 and calificacion < 3:
        grupo3.append(calificacion)
 elif calificacion >= 3 and calificacion < 4:
        grupo4.append(calificacion)
 else:
        grupo5.append(calificacion)

promedio_aprobados = statistics.mean(aprobados)
promedio_reprobados = statistics.mean(reprobados)

print("Calificaciones")
