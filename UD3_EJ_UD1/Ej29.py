import random


n=int(random.random()*100)
print(n)

while True:
    n2=int(input("Intenta adivinar el numero: "))

    if n2>n:
        print("el numero buscado es menor")
    elif n2<n:
        print("el numero buscado es mayor")
    else:
        print("acertaste")
        break