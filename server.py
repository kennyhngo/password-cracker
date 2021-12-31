# Low level security of a server that holds passwords
import string

allowed_characters = string.punctuation
password_database = {}
assigned_user_id = 1
# when the user is prompted to input a password, it gets stored into the database


# This is a much more brute force-like and more realistic way of guessing the password
# But we will explore a different approach that's more efficient than this
    # def check_password(user, guess):
    #     actual = password_database[user]
    #     return actual == guess

def get_username() -> str:
    user_name = input("Enter your username: ")

    if user_name == "":
        global assigned_user_id
        user_name = "user" + str(assigned_user_id)
        assigned_user_id += 1

    if user_name == ':q':
        print("Exited Program Successfully.")
        quit()

    if user_name == 'h':
        from main import help
        while user_name == 'h':

            if user_name == 'h':
                help()
            
            user_name = input("Enter your username: ")
            
            if user_name == ':q':
                print("Exited Program Successfully.")
                quit()


    return user_name

def prompt_id(show_password=False) -> str:
    from getpass import getpass

    print("Leave empty for computer-assigned username.")
    user_name = get_username()

    if show_password:
        user_password = input("Enter your password: ")
    else:
        user_password = getpass("Enter your password: ")
    
    current_user = {user_name:user_password}
    password_database.update(current_user)

    return user_name