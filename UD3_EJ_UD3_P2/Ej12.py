print("introduce un numero:")
n=int(input())

for i in range(1,n+1):
    numero=str(i)
    for j in range(1,i):
        numero+=str(i)
    print(numero)