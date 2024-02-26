def password_exists(password):
    with open("passwords.txt", "r") as file:
        existing_passwords = [line.strip() for line in file]
        if password in existing_passwords:
            return True
        else:
            return False


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
        if not any(val.isupper() for val in password):
            print("Passwords needs to have at least one uppercase character.")
        if not any(val.islower() for val in password):
            print("Password needs to have at least one lowercase character.")
        else:
            return password


def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(f"{password}\n")
    print("Password saved")


username = create_username()
password = create_password()
if not password_exists(password):
    save_password(password)
else:
    print("Password already exists. Please choose another password.")


