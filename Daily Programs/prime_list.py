#a,b=map(int,input("Enter Numbers Range:").split())

#for i in range(a,b+1):
#    N=0
#    for j in range(1,i+1):
#        if i%j==0:
#            N +=1
#    if N == 2:     
#        print(i)



a = int(input("Enter starting number"))
b = int(input("Enter ending number"))
for n in range(a,b+1): 
    y = 0
    for i in range (2,(n//2)+1):
        if n%i == 0:
            y +=1
    if y == 0:
        print(n)









#a = int(input("Enter starting number"))
#b = int(input("Enter ending number"))
#while a <= b:
#    y = 0
#    for i in range(2, (a // 2) + 1):
#        if a % i == 0:
#            y += 1
#    if y == 0:
#        print(a)
#    a += 1

