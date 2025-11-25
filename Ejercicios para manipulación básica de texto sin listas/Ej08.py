texto = input("Introduce tu frase: ")
resultado = ""

for i in texto:
    codigo = ord(i)

    if 97 <= codigo <= 122:
        resultado += chr(codigo - 32)
    else:
        resultado += i

print(resultado)