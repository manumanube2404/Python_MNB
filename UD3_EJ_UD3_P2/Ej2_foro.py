print("Introduce un numero:")
numero=int(input())
espacios=" "
print(str(numero-1))

for i in range (1,numero-1):
    print(str(numero-1)+espacios*(i)+str(numero-1))
    if i==numero-2:
        print(str(numero-1)*numero)