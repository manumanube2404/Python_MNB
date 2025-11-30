base=int(input("Introduce la base: "))
exponente=int(input("Introduce el exponente: "))

potencia=1

for i in range(exponente):
    potencia*=base
print(potencia)