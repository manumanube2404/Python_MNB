print("introduce un numero")
n=int(input())
asterisco="*"
espacio="."


for i in range(3):
    print(espacio*(i)+asterisco+espacio*(((n//2)-i)-1)+asterisco+espacio*(((n//2)-i)-1)+asterisco+espacio*(i))
print(asterisco*n)

for j in range(3,0,-1):
    print(espacio*(j-1)+asterisco+espacio*(((n//2)-j))+asterisco+espacio*(((n//2)-j))+asterisco+espacio*(j-1))