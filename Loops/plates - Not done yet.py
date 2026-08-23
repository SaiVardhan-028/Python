def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if plate == Hello or plate == CS50:
        print("Valid")
    else:
        print("Invalid")


main()