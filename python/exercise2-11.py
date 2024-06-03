phase = input("Is the moon full? If yes enter Full if no enter No: ")
distance = int(input("Enter the distance of the moon from the earth: "))
date = int(input("Enter the date of the month: "))
eclipse = input("Is there an eclipse? Enter True for yes and False for no:")
if phase != "Full":
    print("Moon")
else:
    if eclipse == "True":
        if distance < 230000: 
            if date == 29 or date == 30 or date == 31:
                print("Super Blue Blood Moon")
            else:
                print("Super Blood Moon")
        else:
            if date == 29 or date == 30 or date == 31:
                print("Blue Blood Moon")
            else:
                print("Blood Moon")
    else:
        if distance < 230000:
            if date == 29 or date == 30 or date == 31:
                print("Super Blue Moon")
            else:
                print("Super Moon")
        else:
            if date == 29 or date == 30 or date == 31:
                print("Blue Moon")
            else:
                print("Moon")

