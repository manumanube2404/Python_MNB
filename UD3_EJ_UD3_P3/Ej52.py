n = int(input("Introduce el número de empleados: "))
precio_hora = int(input("Introduce el precio por hora (€): "))
total_empresa = 0

for i in range(1, n + 1):
    horas = int(input(f"Introduce las horas trabajadas por el empleado {i}: "))
    sueldo = horas * precio_hora
    total_empresa += sueldo
    print(f"Sueldo del empleado {i}: {sueldo:} €\n")

print(f"Total pagado por la empresa: {total_empresa:} €")
