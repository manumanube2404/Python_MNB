alumnos = int(input("Introduce el número de alumnos: "))

# Determinar el costo según la cantidad
if alumnos >= 100:
    costo_por_alumno = 65
    total = alumnos * costo_por_alumno

elif 50 <= alumnos <= 99:
    costo_por_alumno = 70
    total = alumnos * costo_por_alumno

elif 30 <= alumnos <= 49:
    costo_por_alumno = 95
    total = alumnos * costo_por_alumno  
else:
     print("Costo individual por alumno:", 4000 / alumnos, "€")


if alumnos>30:
    print("Costo por alumno:", costo_por_alumno, "€")
    print("Total a pagar por el grupo:", total, "€") 
