print("Introduce un numero del 1 al 10:")
n=int(input())
match n:
    case _ if n>=0 and n<3:
        print(" Muy Deficiente")
    case _ if n>=3 and n<5:
        print(" Insuficiente")
    case _ if n>=5 and n<6:
        print(" Suficiente")   
    case _ if n>=6 and n<7:
        print(" Bien")
    case _ if n>=7 and n<9:
        print(" Notable")
    case _ if n>=9 and n<=10:
        print(" Sobresaliente")