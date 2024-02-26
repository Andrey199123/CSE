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


create_username()
save_password(create_password())
