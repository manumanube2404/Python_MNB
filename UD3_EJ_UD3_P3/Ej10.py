parcial1 = float(input("Introduce la calificación del parcial 1: "))
parcial2 = float(input("Introduce la calificación del parcial 2: "))
parcial3 = float(input("Introduce la calificación del parcial 3: "))

examen_final = float(input("Introduce la calificación del examen final: "))
trabajo_final = float(input("Introduce la calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("Tu calificación final es:", calificacion_final)
