# Forma 1
# print("Introduce un numero")
# altura=int(input())
# for i in range(1,altura+1):
#     for j in range(0,i-1):
#         print(" ",end="")
#     for k in range(0,(2*altura+1)-(i*2)):
#         print("*",end="")
#     print("")

#Forma 2
# print("Introduce un numero")
# altura=int(input())
# for i in range(1,altura+1):
#     print(" "*(i-1),"*"*((2*altura+1)-(i*2)))

print("dame la altura de la piramide")
altura=int(input())
for i in range(0,altura):
    asterisco="*"*(((altura-i)*2)-1)
    
    espacios=" "*i
    
    print(espacios+asterisco)