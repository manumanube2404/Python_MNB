import random


n=round(random.random()*100)
acierto=False
intentos=0
while acierto==False and intentos<10:
    intentos+=1
    n2=int(input("introduce un numero: "))
    if n2>n:
        print("el numero es menor")       
    elif n2<n:
        print("el numero es mayor")  
    else:
         print("acertaste")
         acierto=True  

if intentos==10:
    print("El numero era: ",n)