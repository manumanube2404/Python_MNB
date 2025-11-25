frase=input("Introduce su frase: ")
letra=input("introduce el caracter que quiere cambiar: ")
nueva_fras=""
letra2=input("introduce la letra que quieres cambiar: ")
for i in range(len(frase)):
    
    if frase[i].lower()!=letra.lower():
        nueva_fras+=frase[i]
    else:
        nueva_fras+=letra2
print(nueva_fras)