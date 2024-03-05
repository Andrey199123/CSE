import pickle

try:
  with open("passwords.pkl", "rb") as file:
    passwords = pickle.load(file)
except FileNotFoundError:
  passwords = {}
  
def create_account():
    while True:
        username = input("Enter your username: ")
        if "@" in username and "." in username:
            break
        else:
            print("Invalid username.")
    while True:
      password = input("Enter your password: ")
      if len(password) < 8:
          print("Password needs to be at least 8 characters long.")
      if not any(val.isupper() for val in password):
          print("Passwords needs to have at least one uppercase character.")
      if not any(val.islower() for val in password):
          print("Password needs to have at least one lowercase character.")
      else:
          passwords[username] = password
          print("Account created successfully.")
          break

def look(passwords):
    username = input("Enter the username (email address): ")
    if username in passwords:
        print("Password:", passwords[username])
    else:
        print("Username not found.")

def save_password(passwords):
      with open("passwords.pkl", "wb") as file:
        pickle.dump(passwords, file)

def change(passwords):
  username = input("Enter the username (email address): ")
  if username in passwords:
      new_password = input("Enter the new password: ")
      passwords[username] = new_password
      print("Password changed successfully.")
  else:
      print("Username not found.")

def delete(passwords):
  username = input("Enter the username (email address) to delete: ")
  if username in passwords:
      del passwords[username]
      print("Username and password deleted successfully.")
  else:
      print("Username not found.")


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


while True:
  menu = input("Type 'look' to look up a person's password, 'add' to add a new username and password, 'change' to change an existing password, 'delete' to delete an existing username and password, or 'quit' to quit:")
  if menu == "look":
    look(passwords)
  elif menu == "add":
    create_account()
    save_password(passwords)
  elif menu == "change":
    change(passwords)
  elif menu == "delete":
    delete(passwords)
  elif menu == "quit":
    break
