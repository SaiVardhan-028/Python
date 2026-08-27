def main():
    x = Item()
    Calories(x)

def  Item():
    return input("Item:").lower()

def Calories(x):
    fruits = { "apple" : 130,
            "avacado" : 110,
            "sweet cherries" : 50
            }
    if x in fruits:
        print("Calories",fruits[x])
    else:
        print("No Calories",end="")

main()
