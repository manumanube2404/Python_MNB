nota =0
_10=0
while nota!= -1:
    print("Introduce una nota del 0 al 10 (o -1 para terminar):")
    nota=int(input())
    if nota==10:
        _10+=1
print(f"Has introducido {_10} notas de 10")