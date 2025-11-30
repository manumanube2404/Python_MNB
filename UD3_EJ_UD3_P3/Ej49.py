precio_hora = int(input("Introduce el precio por hora (€): "))
total_horas = 0

for dia in range(1, 7):  
    horas = int(input(f"Introduce las horas trabajadas el día {dia}: "))
    total_horas += horas

sueldo = total_horas * precio_hora

print(f"Total de horas trabajadas: {total_horas} horas")
print(f"Sueldo a recibir: {sueldo} €")