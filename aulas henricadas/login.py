from os.path import exists

directory = 'files/passwords.txt'
if exists(directory):
    my_user = input("user: ").strip()
    my_password = input("password: ").strip()

    with open(directory, 'r') as text_file:
        for content in text_file:
            user, password = content.strip().split(",")
            
            if my_user == user:
                if my_password == password:
                    print("logged successfuly")
                    break
                print("passwords didn't match")
                break
            print("user not found")
            break

else:
    print("Passwords.txt is missing.")
