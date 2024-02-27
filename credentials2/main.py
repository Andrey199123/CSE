import sys
def create_username():
    while True:
        username = input("Enter your username: ")
        if "@" in username and "." in username:
            return username
        else:
            print("Invalid username.")


def create_password():
    while True:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Password needs to be at least 8 characters long.")
            sys.exit(0)
        if not any(val.isupper() for val in password):
            print("Passwords needs to have at least one uppercase character.")
            sys.exit(0)
        if not any(val.islower() for val in password):
            print("Password needs to have at least one lowercase character.")
            sys.exit(0)
        else:
            return password


def save_password(password):
    try:
        with open("passwords.txt", "a") as file:
            file.write(f"{password}\n")
        print("Password saved")
    except:
        with open("passwords.txt", "x") as file:
            file.write(f"{password}\n")
        print("Password saved")


def password_exists(password):
    try:
        try:
            with open("passwords.txt", "r") as file:
                passwords = file.readlines()
        except:
            with open("passwords.txt", "x") as file:
                passwords = file.readlines()
        for passwd in passwords:
            if passwd.strip() == password:
                return True
    except:
        return False

create_username()
password = create_password()
if password_exists(password):
    print("Password already exists")
else:
    save_password(password)
    print("Password created.")
