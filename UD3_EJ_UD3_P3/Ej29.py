a=int(input("introduce el lado a: "))
b=int(input("introduce el lado b: "))
c=int(input("introduce el lado c: "))
iguales=-2
mahoraga=[a,b,c]

for i in range(3):
    for j in range(3):
        if mahoraga[i]==mahoraga[j]:
            iguales+=1
         
    
match iguales:
    case _ if c**2==(a**2)+(b**2):
        print("es un triangulo rectangulo")
    case 1:
        print("es un triangulo escaleno")
    case 3:
        print("es un triangulo isosceles")
    case _ if iguales>3:
        print("es un triangulo equilatero")
    