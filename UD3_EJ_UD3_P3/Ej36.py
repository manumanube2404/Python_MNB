mes = int(input("Introduce un número del 1 al 12: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Este mes tiene 31 días.")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Este mes tiene 30 días.")

elif mes == 2:
    print("Febrero tiene 28 días (29 si es año bisiesto).")

else:
    print("Error: número fuera de rango (1-12).")
