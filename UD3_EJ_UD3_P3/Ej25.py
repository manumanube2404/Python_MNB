texto=input("introduce un texto: ")

for i in range(len(texto)):
    if texto[i].isupper():
        print(f"El texto tiene mayúsculas en la posición {i}")
        
