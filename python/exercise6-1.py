def clean_user(L):
    cleaned_list = []
    for username in L:
        if "c" in username or "g" in username or "z" in username or "C" in username or "G" in username or "Z" in username:
            continue
        else:
            cleaned_list.append(username)
            return cleaned_list

def main():
    input_list = []
    for i in range(5):
        i = input("username:")
        input_list.append(i)
    print(input_list)
    new_list = clean_user(input_list)
    print(new_list)

main()