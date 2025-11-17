# print("Introduce un numero")
# altura=int(input())
# for i in range(1,altura+1):
#     for j in range(0,i-1):
#         print(" ",end="")
#     for k in range(0,(2*altura+1)-(i*2)):
#         print("*",end="")
#     print("")

print("Introduce un numero")
altura=int(input())
for i in range(1,altura+1):
    print(" "*(i-1),"*"*((2*altura+1)-(i*2)))