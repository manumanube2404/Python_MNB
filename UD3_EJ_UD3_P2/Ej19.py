print("piensa un numero entre 1 y 100")
minimo=1
maximo=100
while True:
    intento=(minimo+maximo)//2
    print("¿es",intento,"tu numero?")
    print("1. si")
    print("2. no, es mayor")
    print("3. no, es menor")
    respuesta=int(input())
    if respuesta==1:
        print("he adivinado tu numero:",intento)
        break
    elif respuesta==2:
        minimo=intento+1
    elif respuesta==3:
        maximo=intento-1
                
    