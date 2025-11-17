# print("Introduce un numero")
# altura=int(input())
# for i in range(1,altura+1):
    
#     for j in range(i,altura):
#         print(" ",end="")
    
#     for k in range(1,2*i):
#         print("*",end="")
#     print("")

print("introduce un numero:") 
altura=int(input())
for i in range(1,altura+1):
    asteriscos=str("*"*(i*2-1))
    
    espacios=str(" "*(altura-i))
    print(espacios+asteriscos)