
while True:
    letras=input("Introduce una letra: ")
    if letras in "aeiouAEIOU":
        print("Es una vocal")
    elif letras==" ":
        print("No has introducido una letra")
        break
    else: 
        print("No es una vocal")