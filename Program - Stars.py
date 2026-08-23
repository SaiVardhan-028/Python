def main():
    Triangle(8)
    
def Triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print("*",end="")
        print()
main()