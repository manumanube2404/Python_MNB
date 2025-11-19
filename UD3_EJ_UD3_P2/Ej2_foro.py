print("Introduce un numero:")
numero=int(input())
espacios=" "
print(str(numero))

for i in range (1,numero-1):
    print(str(numero)+espacios*(i)+str(numero))
    if i==numero-2:
        print((str(numero)+espacios)*numero)