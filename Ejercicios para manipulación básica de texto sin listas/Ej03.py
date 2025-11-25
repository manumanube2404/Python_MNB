letra=input("introduce su letra: ")
frase=input("Introduce su frase: ")
contador = 0
for i in range(len(frase)):
    if frase[i].lower()==letra.lower():
        contador+=1

print(f"Hay {contador} {letra} en tu frase")