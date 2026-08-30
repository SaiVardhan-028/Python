#n = int(input("Enter Number: "))

#x = 1
#for i in range(1, n+1):
#    x *= i
#print(x)



n = int(input("Enter Number: "))

x = 1 
while n > 0:
    x = n * x
    n = n - 1
print(x)