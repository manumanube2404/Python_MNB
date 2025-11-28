minutos=int(input("introduzca los minutos"))
horas=0

while minutos>=60:
    horas+=1
    minutos-=60

print(f"horas: {horas}, minutos: {minutos}")