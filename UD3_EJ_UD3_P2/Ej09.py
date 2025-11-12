print("introduzca numeros, para parar introduzca 0")
pos=0
neg=0

while True:
    n=int(input())
    if n>0:
        pos+=1
    elif n<0:
        neg+=1
    else:
        break

print(f" ha leido {pos} positivos y {neg} negativos")