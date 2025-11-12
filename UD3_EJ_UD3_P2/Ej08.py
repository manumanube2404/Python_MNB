print("introduzca 100 numeros:")
neg=0
pos=0

for i in range(1,5):
    n=int(input())
    if n<0:
        neg+=1
    else:
        pos+=1

print(f"Han salido {neg} negativos y {pos} positivos")