print("Introduzca el precio inicial:")
precio=int(input())

print("Introduzca el dia de la semana:")
dia=input()

if dia=="martes" or dia== "jueves":
    precio-=(precio*0.15)

print(f"Precio final: {precio}")