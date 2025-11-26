frase=input("introduce una frase: ")
n_frase=""

for i in range(len(frase)-1,-1,-1):
    n_frase+=frase[i]

print(n_frase)