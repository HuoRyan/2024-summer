score = int(input("Score:"))
#while True:
#    if score >= 0 and score <= 100:
#        break
 #   else:
 #       score = int(input("Invalid input. Please enter a score between 0 and 100.n/Score:"))
while score < 0 or score > 100:
    score = int(input("Invalid input. Please enter a score between 0 and 100.n/Score:"))

if score >= 95:
    print('A')
elif score >= 90:
    print('A-')
elif score >= 87:
    print('B+')
elif score >= 83:
    print( 'B')
elif score >= 80:
    print('B-')
elif score >= 77:
    print('C+')
elif score >= 73:
    print('C')
elif score >= 70:
    print('C-')
elif score >= 67:
    print('D+')
elif score >= 63:
    print('D')
elif score >= 0:
    print('F')
   

