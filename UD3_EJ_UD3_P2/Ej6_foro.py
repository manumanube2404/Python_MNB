print("introduce un numero")
n=int(input())
asterisco="*"
espacio=" "
mitad=n//2
k=n-2
print(asterisco+espacio*(n-2)+asterisco)
for i in range(mitad-1):
        k-=2
        print(asterisco+espacio*i+asterisco+espacio*(k)+asterisco+espacio*(i)+asterisco)
print(asterisco+espacio*(mitad-1)+asterisco+espacio*(mitad-1)+asterisco)        

for j in range(mitad):
    print(asterisco+espacio*(n-2)+asterisco)