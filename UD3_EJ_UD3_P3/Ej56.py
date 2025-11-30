def es_primo(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


n = int(input("¿Cuántos números primos quieres mostrar? "))

contador = 0
num = 2

while contador < n:
    if es_primo(num):
        print(num)
        contador += 1
    num += 1
