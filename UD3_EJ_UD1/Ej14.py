print("introduzca 2 numeros:")
num1=int(input())
num2=int(input())
suma=num1+num2
resta=num1-num2
producto=num1*num2
if num2!=0:
    division=num1/num2
else:
    division="Error, no se puede dividir por cero"
print("La suma es:",suma,"la resta es:",resta,"el producto es:",producto,"la division es:",division)