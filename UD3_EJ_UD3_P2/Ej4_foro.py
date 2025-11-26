n=int(input("Introduce un numero: "))
asterisco="*"
espacio=" "

print(asterisco*n)

k=n//2
f=2

for i in range(1,(n//2)+1):
    print(asterisco+(espacio*i)+asterisco+(espacio*k)+asterisco)
    k-=1

for j in range(((n//2)-1),0,-1):
    print(asterisco+(espacio*j)+asterisco+(espacio*f)+asterisco)
    f+=1

print(asterisco*n)