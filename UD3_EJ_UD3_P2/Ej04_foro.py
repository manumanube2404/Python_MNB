print("numero:")
num=int(input())
asterisco="*"
espacio=" "


for i in range(num):
    print(asterisco*(num*2)+asterisco)
    print((asterisco+espacio)*num+asterisco)