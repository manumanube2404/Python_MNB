letra=input("introduce su letra: ")
frase=input("Introduce su frase: ")
aparece = False
for i in range(len(frase)):
    if frase[i].lower()==letra.lower():
        aparece=True

if aparece:
    print(f"La letra {letra} aparece en la frase")
else:
    print(f"La letra {letra} no aparece en la frase")