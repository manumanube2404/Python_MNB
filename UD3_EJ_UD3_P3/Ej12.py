import math
x1=float(input("Introduce la coordenada x del primer punto: "))
y1=float(input("Introduce la coordenada y del primer punto: "))
x2=float(input("Introduce la coordenada x del segundo punto: "))
y2=float(input("Introduce la coordenada y del segundo punto: "))
distancia=math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los puntos es: {distancia} unidades")