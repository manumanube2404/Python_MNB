print("introduce un numero")

n=int(input())
asterisco="*"
espacio=" "
print(asterisco*n)
for i in range((n-2)):
    if i==0 or i==(n//2)-1:
        print((asterisco+espacio)*(n//2)+asterisco)
    if i!=n-1:
        print(asterisco+espacio*(n-1)+asterisco)
print(asterisco*n)