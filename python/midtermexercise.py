Socialsecuritynumber = input("Social security number:")
if Socialsecuritynumber[0] == 1:
    print("Gender is male" )
else:
    print("Gender is female ")
print("Year of birth is" + Socialsecuritynumber[1:3])
print("Month of birth is " + Socialsecuritynumber[3:5])
department_of_birth = Socialsecuritynumber[5:7]
if department_of_birth == '99':
        country_of_birth = "Outside France"
        commune_of_birth = "Outside France"
        print(country_of_birth)
        print(commune_of_birth)
else:
    if int(department_of_birth) >= 97 and int(department_of_birth) <= 99:
            country_of_birth = "Oversea France"
            print(country_of_birth)
    else:
        country_of_birth = "France"
        commune_of_birth = Socialsecuritynumber[7:10]
        print(country_of_birth)
        print(commune_of_birth)
    
birth_order = Socialsecuritynumber[10:13]
control_key = Socialsecuritynumber[13:15]
print(birth_order)
print(control_key)
calculated_key = 97 - (int(Socialsecuritynumber[:13]) % 97)

if calculated_key != int(control_key):
    print("Social security number is not valid")