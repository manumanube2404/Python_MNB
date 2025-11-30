minutos = int(input("Duración de la llamada en minutos: "))
dia = input("¿Es domingo? (si/no): ")
turno = None

if dia != "si":
    turno = input("Turno (mañana/tarde): ")

costo = 0

if minutos <= 5:
    costo = 1
elif minutos <= 8:
    costo = 1 + (minutos - 5) * 0.80
elif minutos <= 10:
    costo = 1 + (3 * 0.80) + (minutos - 8) * 0.70
else:
    costo = 1 + (3 * 0.80) + (2 * 0.70) + (minutos - 10) * 0.50


if dia == "si":
    impuesto = 0.03   
else:
    if turno == "mañana":
        impuesto = 0.15
    else:
        impuesto = 0.10

total = costo + (costo * impuesto)

print(f"Costo base de la llamada: {costo} €")
print(f"Impuesto aplicado: {impuesto*100}%")
print(f"Total a pagar: {total} €")
