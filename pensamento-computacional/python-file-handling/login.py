from os.path import exists
from getpass import getpass

def main():
    directory = 'files/passwords.txt'
    if not exists(directory):
        print("Passwords.txt is missing.")
        return

    my_user = input("user: ").strip()
    my_password = getpass("password: ").strip()

    with open(directory, 'r') as text_file:
        corret_fields = False
        for content in text_file:
            user, password = content.strip().split(",")
            
            if my_user == user and my_password == password:
                corret_fields = True
                print("logged successfully")
                break

        if not corret_fields:
            print("user not found or wrong password")

if __name__ == "__main__":
    main()

