distancia = float(input("Introduce la distancia entre los vehículos (km): "))
v1 = float(input("Introduce la velocidad del vehículo de adelante (km/h): "))
v2 = float(input("Introduce la velocidad del vehículo de atrás (km/h): "))

tiempo_horas = distancia / (v2 - v1)

tiempo_minutos = tiempo_horas * 60

print("El vehículo más rápido alcanzará al otro en:", tiempo_minutos, "minutos")