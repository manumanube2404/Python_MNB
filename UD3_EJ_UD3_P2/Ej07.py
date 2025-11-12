print("introduzca 100 numeros:")
neg=False
for i in range(1,5):
    n=int(input())
    if n<0:
        neg=True

if neg:
    print("Ha salido un numero negativo")
else:
    print("No ha salido ningun numero negativo")