frase=input("introduce una frase: ")
n_frase=""
vocales=["a","e","i","o","u"]

for i in range(len(frase)):
    n_frase+=frase[i]
    for j in range(len(vocales)):
        if frase[i]==vocales[j]:
            n_frase+=frase[i]

print(n_frase)