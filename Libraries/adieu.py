names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

if len(names) == 1:
    result = names[0]
elif len(names) == 2:
    result = " and ".join(names)
else:
    result = ", ".join(names[:-1]) + ", and " + names[-1]

print("Adieu, adieu, to", result)