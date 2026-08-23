def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Must be between 2 and 6 characters
    if not 2 <= len(s) <= 6:
        return False

    # Must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Only letters and numbers are allowed
    if not s.isalnum():
        return False

    # Once a number appears, no letters can appear afterward
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and i == 2:
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


if __name__ == "__main__":
    main()