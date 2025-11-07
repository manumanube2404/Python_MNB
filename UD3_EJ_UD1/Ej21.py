print("introduce un numero:")
Neg=False

for i in range(1, 5):
    numero = int(input())
    if numero < 0:
        Neg=True

if Neg:
    print("Ha introducido un numero negativo")
else:
    print("No ha introducido ningun numero negativo")