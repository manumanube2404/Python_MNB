dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

correcta = True

if mes < 1 or mes > 12:
    print("El mes es invalido")

else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia>=1 and dia<31:
            print("El mes es invalido")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia>=1 and dia<30:
            print("El mes es invalido")

    elif mes == 2:
        if dia>=1 and dia<29:
            print("El mes es invalido")