horas = float(input("Horas trabajadas en la semana: "))
tarifa = float(input("Tarifa por hora (€): "))

if horas <= 35:
    bruto = horas * tarifa
else:
    horas_normales = 35
    horas_extra = horas - 35
    bruto = (horas_normales * tarifa) + (horas_extra * tarifa * 1.5)

impuesto = 0

if bruto > 900: 
    impuesto += (bruto - 900) * 0.45
    impuesto += 400 * 0.25
elif bruto > 500:
    impuesto += (bruto - 500) * 0.25

neto = bruto - impuesto

print(f"Salario bruto: {bruto} €")
print(f"Impuestos: {impuesto} €")
print(f"Salario neto: {neto} €")