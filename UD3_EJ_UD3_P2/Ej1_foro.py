print("Introduce un numero:")
numero=int(input())
asterisco="*"
espacios=" "
print(espacios*(numero+1)+asterisco)
for i in range (1,numero):
    print(espacios*(numero-i)+asterisco+espacios*(i)+asterisco)


for j in range (numero,0,-1):
    print(espacios*(numero-j)+asterisco+espacios*(j)+asterisco)
   
print(espacios*(numero+1)+asterisco)
    
#
#      *
#     **
#    * * 
#   *  *
#  *   *
# *    *
#
#
#
#
#