base=int(input("Introduce la base: "))
exponente=int(input("Introduce el exponente: "))

match exponente:
    case _ if exponente>0:
        print(base**exponente)
    case _ if exponente==0:
        print(1)    
    case _ if exponente<0:
        print(1/(base**exponente))

