a,b,c=input("Expression:").split()

a =int(a)
c =int(c)

if b == "+":
    result = a+c
elif b == "-":
    result = a-c
elif b == "*":
    result = a*c
elif b == "/":
    result = a/c
else:
    result = a%c

print(f"{result:.1f}")

