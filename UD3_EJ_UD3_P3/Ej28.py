n1=int(input("numero 1: "))
n2=int(input("numero 2: "))
n3=int(input("numero 3: "))

f=0
ordenado=[n1,n2,n3]

for i in range(3):
    for j in range(3):
        if ordenado[i]>=ordenado[j]:
            f=ordenado[i]
            ordenado[i]=ordenado[j]
            ordenado[j]=f
print(ordenado)
            