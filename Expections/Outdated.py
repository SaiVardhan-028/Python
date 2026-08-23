months = ["January",
        "February", 
        "March", 
        "April",
        "May",
        "June", 
        "July",
        "August",
        "September",
        "October", 
        "November",
        "December"]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month, day_year = date.split(" ")
            day, year = day_year.split(",")
            month = months.index(month) + 1
            day = int(day)
            year = int(year)

        if month < 1 or month > 12 or day < 1 or day > 31:
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        continue