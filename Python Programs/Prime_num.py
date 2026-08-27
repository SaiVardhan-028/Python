X = int(input("enter number:"))

countprime=0
for i in range(1,X+1):
    N=0
    for j in range(1,i+1):
        if i%j==0:
            N +=1
    if N==2:
        countprime +=1
print(countprime)