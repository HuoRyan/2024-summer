userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'], ['likeA', 'pwd3AAAAAAA'], ['qwerty', 'pwd4QWERTY']]
def valid_username(username, nameList):
    for user in nameList:
        if username == user[0]:
            return "username is exist", False
    if len(username) < 5:
        return "invalid", False
    else:
        return "valid", True

def valid_password(password):
    if len(password) < 8:
        return "invalid", False
    char_upper = False
    char_lower = False
    char_digit = False
    for char in password:
        if char.isupper():
            char_upper = True
        if char.islower():
            char_lower = True
        if char.isdigit():
            char_digit = True
    if not (char_upper and char_lower and char_digit):
        return "invalid", False
    return "valid", True

def add_user(userList):
    while True:
        username = input("Enter Username: ")
        message, valid = valid_username(username, userList)
        print(message)
        if valid:
            break
    while True:
        password = input("Enter Password: ")
        message, valid = valid_password(password)
        print(message)
        if valid:
            confirm_password = input("Confirm Password: ")
            if password == confirm_password:
                userList.append([username, password])
                print("User created")
                break
            else:
                print("Passwords do not match")
            
print(valid_username("likeA", userList))
print(valid_password('azertyuiop'))
add_user(userList)
print(userList)