a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for i in range (a,b+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count +=1
    if count == 2:
        print(f"{i} is prime")
    else:            
        print(f"{i} is not prime")
        
        
#a = int(input("Enter starting number: "))
#b = int(input("Enter ending number: "))

#while a<b:
#    count = 0
#    for i in range (1,a+1):
#        if a%i == 0:
#            count +=1
#    if count == 2:
#        print(f"{i} is prime")
#    else:            
#        print(f"{i} is not prime")
#    a +=1