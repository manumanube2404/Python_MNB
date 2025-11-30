pago = 10  
total = 0

for i in range(1, 21):
    print(f"Mes {i}: {pago} €")
    total += pago
    pago *= 2  

print(f"\nTotal pagado después de 20 meses: {total} €")