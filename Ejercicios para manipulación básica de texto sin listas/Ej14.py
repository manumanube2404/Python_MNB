texto=input("introduce una cadena de texto: ")
numeros=["0","1","2","3","4","5","6","7","8","9"]
contador=0
for i in range(len(texto)):
    for j in range(len(numeros)):
        if texto[i]==numeros[j]:
            contador+=1

print(f"han aparecido {contador} numeros")