while True:
    linf=int(input("Introduce el limite inferior: "))
    lsup=int(input("Introduce el limite superior: "))
    if lsup>linf:
        break
    else:
        print("Error")
suma=0
fuera=0
igual=False
while True:
    n=int(input("intoduce un numero"))
    if n==0:
        break
    else:
        if n>linf and n<lsup:
            suma+=n
        elif n==linf or n==lsup:
            igual=True
        else:
            fuera+=1
print(f"Suma de los numeros dentro del rango: {suma}, Numeros iguales a los limites: {igual}, Numeros fuera del rango: {fuera}")