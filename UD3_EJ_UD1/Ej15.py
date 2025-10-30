from math import e


print("introduzca 3 numeros:")
num1=int(input())
num2=int(input())
num3=int(input())
if num1>=num2:
    if num1==num2:
        print(num1,"y",num2,"son iguales")
        if num1>=num3:
            if num1==num3:
                print("Los tres numeros son iguales")
            else:
                print(num1,"y",num2,"son los mayores y",num3,"es el menor")
        else:
            print(num3,"es el mayor y",num1,"y",num2,"son los menores")
    else:
        if num2>=num3:
            if num2==num3:
                print(num2,"y",num3,"son iguales")
                print(num1,"es el mayor y",num2,"y",num3,"son los menores")
            else:
                print(num1,"es el mayor y",num3,"es el menor")
        else:
            if num1==num3:
                print(num1,"y",num3,"son iguales")
                print(num1,"y",num3,"son los mayores y",num2,"es el menor")
            elif num1>num3:
                print(num1,"es el mayor y",num2,"es el menor")
            else:
                print(num3,"es el mayor y",num2,"es el menor")
else:
    if num2>=num3:
        if num2==num3:
            print(num2,"y",num3,"son iguales")
            print(num2,"y",num3,"son los mayores y",num1,"es el menor")
        else:
            if num1>=num3:
                if num1==num3:
                    print(num2,"es el mayor y",num1,"y",num3,"son los menores")
                else:
                    print(num2,"es el mayor y",num3,"es el menor")
            else:
                print(num2,"y",num1,"es el menor")
    else:
        print(num3,"es el mayor y",num1,"es el menor")