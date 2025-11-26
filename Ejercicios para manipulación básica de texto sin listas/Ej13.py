texto=input("introduce su frase: ")
n_tex=""

for i in range(len(texto)):
    if texto[i]!=" ":
        n_tex+=texto[i]

print(n_tex)