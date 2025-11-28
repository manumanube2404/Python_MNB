frase=input("introduce una frase: ")
n_frase=""
letra=[]
repetidas=[]
for i in range(len(frase)):
    letra+=frase[i]

for j in range(len(letra)):
    contador=0
    for k in range(len(letra)):
        if letra[j]==letra[k]:
            contador+=1
            print(n_frase)
    if contador>=2:
        for g in range(n_frase):
            if n_frase.__contains__letra[k]:
                n_frase+=str(letra[j])
        

print(letra)
print("Frase: "+n_frase)



# cadena = input("Introduce una cadena: ")

# nueva = ""

# for i in range(len(cadena)):
#     c = cadena[i]
#     # Si el caracter aparece más de una vez en la cadena
#     if cadena.count(c) > 1:
#         nueva += c

# print("Caracteres que se repiten:", nueva)