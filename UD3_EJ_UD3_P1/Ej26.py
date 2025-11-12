import random


dados=[random.randint(1,6),random.randint(1,6),random.randint(1,6)]
a_6=0

for i in range(0,len(dados)):
    print(dados[i])
    if dados[i]==6:
        a_6+=1

match a_6:
    case 3:
        print("excelente")
    case 2:
        print("muy bien")
    case 1:
        print("regular")
    case _:
        print("pesimo")