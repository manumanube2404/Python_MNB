nota=int(input("introduce su nota: "))
edad=int(input("introduce su edad: "))
sexo=input("introduce su sexo (f/m): ")

match True:
    case _ if nota>=5 and edad>=18 and sexo=="f":
        print("aceptada")
    case _ if nota>=5 and edad>=18 and sexo=="m":
        print("posible")
    case _:
        print("no aceptada")