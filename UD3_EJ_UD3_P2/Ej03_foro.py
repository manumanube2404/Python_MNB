
print("introduce un numero:")
num=int(input())
espacio="   "
asterisco="***"
num2=round(num/2)

for k in range(num2):
    for i in range(3): #asteriscos x
        
        for j in range(num2):
            print(espacio,end="")
            
            if num%2==0 or j!=num2-1 and num%2!=0:    
                print(asterisco,end="")
        print()
        
    if num%2==0 or k!=num2-1 and num%2!=0:
        for s in range(3): #asteriscos Y
                for h in range(num2):
                    
                    print(asterisco,end="")
                    
                    print(espacio,end="")
                print()