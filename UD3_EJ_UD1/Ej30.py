cantidad = int(input("Introduce la cantidad en euros (múltiplo de 5): "))

billetes = [500, 200, 100, 50, 20, 10, 5]


for b in billetes:
    num = cantidad // b
    if num > 0:
        print(f"{num} billete(s) de {b} €")
    cantidad = cantidad % b