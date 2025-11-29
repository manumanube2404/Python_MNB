#Algoritmo que pida dos números e indique si el primero es mayor que el segundo. 

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"El primer número ({num1}) es mayor que el segundo número ({num2}).")
else:
    print(f"El primer número ({num1}) no es mayor que el segundo número ({num2}).")