dinero=1000
print("Bienvenido a su Cajero Virtual")
print("Su saldo actual es:", dinero)

while True:
    print("Elija 1 para ingresar, 2 para retirar y 3 para salir:")
    match int(input()):
        case 1:
            print("Ingrese la cantidad a ingresar:")
            ingreso=int(input())
            dinero+=ingreso
            print("Su nuevo saldo es:", dinero)
        case 2:
            print("Ingrese la cantidad a retirar:")
            retiro=int(input())
            if retiro<=dinero:
                dinero-=retiro
                print("Su nuevo saldo es:", dinero)
            else:
                print("Fondos insuficientes")
        case 3:
            print("Gracias por usar el Cajero Virtual")
            break