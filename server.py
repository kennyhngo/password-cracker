# Low level security of a server that holds passwords
import string

allowed_characters = string.punctuation
password_database = {}
assigned_user_id = 1

# when the user is prompted to input a password, it gets stored into the database

def check_password(user, guess):
    actual = password_database[user]
    return actual == guess

def prompt_id():
    from getpass import getpass

    print("Leave empty for computer-assigned username.")
    user_name = input("Enter your username: ")
    user_password = getpass("Enter your password: ")

    if user_name == "":
        global assigned_user_id
        user_name = "user" + str(assigned_user_id)
        assigned_user_id += 1

    if user_password == ":q":
        print("exited")
        quit()
    
    current_user = {user_name:user_password}
    password_database.update(current_user)
    print(password_database)