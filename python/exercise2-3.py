year = int(input("Year:"))
if year % 4 != 0:
    print("Not leap year")
else:
    if year % 100 == 0 :
        if year % 400 != 0:
            print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Leap year")
if (year-1950) % 4 == 0 and year > 1950:
    print("World Cup year")
if (year-1960) % 4 == 0 and year > 1960:
    print("Euro Cup year")