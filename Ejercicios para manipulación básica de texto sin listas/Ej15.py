frase=input("introduce una frase: ")
n_frase=""
vocales=["a","e","i","o","u"]


for i in range(len(frase)):
    vocal=True
    
    

    for j in range(len(vocales)):
        if frase[i]==vocales[j]:
            n_frase+="*"
            vocal=False

    if vocal:
            n_frase+=frase[i]
        
        
print(n_frase)