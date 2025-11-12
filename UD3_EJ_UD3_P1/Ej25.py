print ("Ingrese su nombre:")
nombre=input()

print("Ingrese su facultad:")
facultad=input()

match facultad:
    case "sistemas":
        matricula=350
        mensualidad=650
    case "derecho":
        matricula=300
        mensualidad=550
    case "naviera":
        matricula=300
        mensualidad=500
    case "pesquera":
        matricula=310
        mensualidad=460
    case "contabilidad":
        matricula=280
        mensualidad=490
    case "administracion":
        matricula=360
        mensualidad=520

Igv=0.18*(matricula+mensualidad)
total=matricula+mensualidad+Igv

print (f"{nombre},de la facultad de {facultad}, su matricula es {matricula}€, su mensualidad es de {mensualidad}€, su igv es de {Igv}€ y el total es de {total}€")