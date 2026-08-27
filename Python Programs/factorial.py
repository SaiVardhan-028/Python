X = int(input("Enter a number: "))

N = 1
for i in range(1, X + 1):
    N *= i

print(X,"!","=", N)
