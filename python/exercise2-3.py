year = int(input("Year:"))
if year % 4 != 0:
    print("Not leap year")
else:
    if year % 100 == 0:
        print("Not leap year")
        if year % 400 == 0:
            print("Leap year")
    else:
        print("Leap year")
if (year-1950) % 4 == 0:
    print("World Cup year")
elif (year-1960) % 4 == 0:
    print("Euro Cup year")