def main():
    time = input("What's time is it?:")
    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("Time for Breakfast")
    elif 12.0 <= time <= 13.0:
        print("Time for Lunch")
    elif 19.0 <= time <= 20.0:
        print("Time for Dinner")
    else:
        print("Today")

def convert(time):
    hours, minutes = time.replace(".", ":").split(":")
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60


if __name__ == "__main__":
    main()

