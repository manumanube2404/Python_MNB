# print("Introduce un numero")
# altura=int(input())
# asterisco="*"
# espacio=" "
# for i in range(1,altura+1,2):
#     divisor=round((altura-i)/2)
#     espacio=" "
#     print(str(divisor*espacio)+asterisco*i)
    
print("Introduce un numero")
altura=int(input())
for i in range(1,altura+1):
    for j in range(i,altura):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print("")
        