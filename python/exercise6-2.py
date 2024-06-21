userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'], ['likeA', 'pwd3AAAAAAA'], ['qwerty', 'pwd4QWERTY']]

def valid_username(username, userList):
    for user in userList:
        if user[0] == username:
            return "User Name Exists", False
    if len(username) < 5:
        return "Invalid", False
    return "Valid", True

def valid_password(password):
    if len(password) < 8:
        return "Invalid", False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if not (has_upper and has_lower and has_digit):
        return "Invalid", False

    return "Valid", True


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

# test
print(userList)
print(valid_username('likeA', userList))
print(valid_username('user', userList))
print(valid_password('azertyuiop'))
print(valid_password('12345AZERTYuiop'))
add_user(userList)
print(userList)