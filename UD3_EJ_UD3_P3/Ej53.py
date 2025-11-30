N = int(input("Introduce el número de empleados: "))
precio_hora = int(input("Introduce el precio por hora (€): "))

total_empresa = 0

for emp in range(1, N + 1):
    dias = int(input("¿Cuántos días trabajó esta semana? "))

    total_horas = 0

    for d in range(1, dias + 1):
        horas = int(input(f"Horas trabajadas el día {d}: "))
        total_horas += horas

    sueldo = total_horas * precio_hora
    total_empresa += sueldo

    print(f"Sueldo semanal del empleado {emp}: {sueldo} €")

print(f"\nTotal pagado por la empresa a todos los empleados: {total_empresa} €")
