#Leer una cadena y contar cuántos caracteres son letras mayúsculas.
texto=input("")
contador=0
for i in texto:

    codigo = ord(i)
    if 65 <= codigo <= 90:
        contador+=1

print(f"habia {contador} mayusculas")