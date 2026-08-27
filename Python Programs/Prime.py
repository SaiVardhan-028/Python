X = int(input("Enter Number:"))
N=0
for i in range(1,X+1):
    if X%i == 0:
        N +=1
if N == 2:
    print("Prime")
else:
    print("Not a prime")
    