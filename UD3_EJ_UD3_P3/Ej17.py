hh = int(input("Introduce las horas (HH): "))
mm = int(input("Introduce los minutos (MM): "))
ss = int(input("Introduce los segundos (SS): "))

T = int(input("Introduce el tiempo de viaje en segundos: "))

salida_segundos = hh * 3600 + mm * 60 + ss

llegada_segundos = salida_segundos + T

llegada_segundos = llegada_segundos % 86400

hora_llegada = llegada_segundos // 3600
minuto_llegada = (llegada_segundos % 3600) // 60
segundo_llegada = llegada_segundos % 60

print(f"{hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")