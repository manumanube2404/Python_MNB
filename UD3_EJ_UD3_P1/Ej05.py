import math


print("Introduzca el radio:")
radio=int(input())
diametro=radio*2
longitud=math.pi*diametro
area=math.pi*radio**2
volumen=(4/3)*math.pi*radio**3
print("la longitud es:",longitud,"el area es:",area,"el volumen es:",volumen)