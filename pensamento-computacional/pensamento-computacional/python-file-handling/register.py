from os.path import exists
from os import makedirs

if not exists('files'):
    makedirs('files')

users = []
passwords = []

while True:
    option = input("1 to register a new user or 0 to exit: ")

    if option == '0':
        print("goodbye")
        break

    if option == '1':
        users.append(input("user: "))
        passwords.append(input("password: "))
        with open('files/passwords.txt', 'a+') as text_file:
            for i in range(len(users)):
                text_file.write(f'{users[i]},{passwords[i]}\n')
        print("user added successfully")

    else:
        print("invalid option")
