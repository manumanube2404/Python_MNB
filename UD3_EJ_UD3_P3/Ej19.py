correctas = int(input("Introduce el número de respuestas correctas: "))
incorrectas = int(input("Introduce el número de respuestas incorrectas: "))

nota_final = (correctas * 5) + (incorrectas * -1) 

print("La nota final del estudiante es:", nota_final)