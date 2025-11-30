import math

n = int(input("introduce un numero: "))
raiz = math.floor(math.sqrt(n))
primo = True
print(math.floor(math.sqrt(n)))


for i in range(2, raiz + 1):
    if n % i == 0:
        primo = False
        break

if primo:
    print("el numero es primo")
else:
    print("el numero NO es primo")
