print("Ingrese un numero:")
n=int(input())
espacio=" "
asterisco="*"

print(espacio*(n)+asterisco)
for i in range(1,n-1):
    print(espacio*(n-i)+asterisco+espacio*(((i)*2)-1)+asterisco)
   
print(espacio+asterisco+espacio*(((n-1)*2)-1)+asterisco)
 
for j in range(1,n-1):
    print(espacio*(j+1)+asterisco+espacio*((((n-j)-1)*2)-1)+asterisco)
print(espacio*(n)+asterisco)