print("introduce un numero")
n=int(input())
asterisco="*"
espacio=" "
mitad=n//2
k=n-4
j=1
print(asterisco*n)
for i in range(1,mitad-1):
        k-=2
        print(asterisco+espacio*i+asterisco+espacio*(k)+asterisco+espacio*(i)+asterisco)

        
print(asterisco+espacio*(mitad-1)+asterisco+espacio*(mitad-1)+asterisco)        
print(asterisco+espacio*(n-2)+asterisco)  
print(asterisco+espacio*(mitad-1)+asterisco+espacio*(mitad-1)+asterisco)

for f in range(2,mitad):
        
        print(asterisco+espacio*(mitad-f)+asterisco+espacio*(j)+asterisco+espacio*(mitad-f)+asterisco)
        j+=2
print(asterisco*n)