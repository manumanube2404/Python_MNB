txt1=input("introduce el texto 1: ")
txt2=input("introduce el texto 2: ")
n_txt=""


for j in range(len(txt1)):
    n_txt+=txt1[j]
for f in range(len(txt2)):
    n_txt+=txt2[f]

print(n_txt)