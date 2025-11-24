print("introduce un numero")
n=int(input())

asterisco="*"
espacio=" "
k=1
print(espacio*(n-1)+asterisco)
for i in range(2,n):
    if i==(n//2)+1:
        print((espacio*(n-i))+(asterisco+espacio)*((n//2)+1))
        k+=2
    else:
        print(espacio*(n-i)+asterisco+espacio*k+asterisco)
        k+=2
    
print(str(asterisco+espacio)*n)

