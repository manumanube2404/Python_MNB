total=0
meses=[]
for i in range(12):
    dinero=int(input("introduce la cantidad de este mes"))
    total+=dinero
    print(f"total actual: {total}")

print(f"total: {total}")