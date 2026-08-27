vowels = "AEIOUaeiou"

def main():
    x = Input()
    Output(x)
    
def Input():
    return  input("Input:")

def Output(x):
    for letter in x:
        if letter not in vowels:
            print(letter.lower(),end="")
    print()

main()
