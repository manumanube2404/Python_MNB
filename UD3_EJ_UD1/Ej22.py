print("introduce un numero:")
Neg=0
Pos=0

for i in range(1, 5):
    numero = int(input())
    if numero < 0:
        Neg += 1
    else:
        Pos += 1

print("Numeros negativos:", Neg)
print("Numeros positivos:", Pos)