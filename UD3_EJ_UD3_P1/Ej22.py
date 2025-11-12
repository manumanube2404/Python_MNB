print("Introduzca la hora:")
hora=int(input())
print("Introduzca los minutos:")
minutos=int(input())
print("Introduzca los segundos:")
segundos=int(input())+1

if segundos>=60:
    segundos-=60
    minutos=minutos+1
if minutos>=60:
    minutos-=60
    hora=hora+1

print("La hora introducida es:",hora,":",minutos,":",segundos)