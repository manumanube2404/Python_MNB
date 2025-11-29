sueldo_base = float(input("Introduce tu sueldo base: "))
venta1 = float(input("Introduce el monto de la venta 1: "))
venta2 = float(input("Introduce el monto de la venta 2: "))
venta3 = float(input("Introduce el monto de la venta 3: "))

comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

total_comisiones = comision1 + comision2 + comision3

total_mes = sueldo_base + total_comisiones

print("Comisiones totales:", total_comisiones)
print("Sueldo total del mes:", total_mes)
