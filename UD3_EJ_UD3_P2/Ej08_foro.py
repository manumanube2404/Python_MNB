print("Ingrese un numero:")
n=int(input())
espacio=" "
asterisco="*"

print(espacio*(n)+asterisco)
for i in range(1,n-1):
    print(espacio*(n-i)+asterisco*((i)*2)+asterisco)
   
print(espacio+asterisco*((n-1)*2)+asterisco)
 
for j in range(1,n-1):
    print(espacio*(j+1)+asterisco*(((n-j)-1)*2)+asterisco)

print(espacio*(n)+asterisco)