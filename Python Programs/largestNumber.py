a,b,c = input("Enter Values:").split()

if a>b and a>c:
    print(a,"is larger")
elif b>a and b>c:
    print(b,"is larger")
elif c>a and c>b:
    print(c,"is larger")
else:
    print("No larger Number")