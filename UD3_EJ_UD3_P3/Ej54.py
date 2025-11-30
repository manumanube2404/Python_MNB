horas=0
minutos=0
seg=0

while True:
    seg+=1
    if seg==60:
        minutos+=1
        seg-=60
    if minutos==60:
        horas+=1
        minutos-=60
    print(f"horas: {horas} minutos: {minutos} segundos: {seg}")