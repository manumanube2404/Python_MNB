n=int(input("introduce el la cantidad de numeros para introducir: "))
mayores=0
menores=0
iguales=0
for i in range(n):
    n2=int(input("introduce el numero: "))
    if n2>0:
        mayores+=1
    elif n2<0:
        menores+=1  
    else:
        iguales+=1

print("Mayores que 0: ",mayores," Menores que 0: ",menores," Iguales a 0: ",iguales)