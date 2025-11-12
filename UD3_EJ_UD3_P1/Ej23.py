print("ingrese el precio del producto:")
precio=int(input())

print("Introduzca si pagara con contacto o con tarjeta:")

match input():
    case "contacto":
        precio=precio-(precio*0.05)
    case "tarjeta":
        precio=precio+(precio*0.03)

print("El precio final es:",precio)