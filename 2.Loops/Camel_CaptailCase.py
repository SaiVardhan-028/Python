def main():
    camel = camel_case()
    snake_case(camel)

def camel_case():
    return  input("camelcase:")

def snake_case(camel):
    for letter in camel:
        print(letter)
        if letter.isupper():
            print("_" + letter.lower(),end="")
        else:
            print(letter,end="")
        print(end="")


main()
