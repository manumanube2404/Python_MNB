texto = input("Introduce tu frase: ")
vocales=["a","e","i","o","u"]
contador=0

for i in range(len(texto)):
    for j in range(len(vocales)):
        if texto[i]==vocales[j]:
            contador+=1
print(f"Tu frase tiene {contador} vocales")