cadena = input("Introduce una cadena: ")

resultado = ""

for c in cadena:
    letra = c.lower()
    # si es letra y NO es vocal
    if letra >= 'a' and letra <= 'z' and letra not in "aeiou":
        resultado += c   # añadimos el carácter original

print("Consonantes:", resultado)