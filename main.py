# Verbose: shows some statistics
# Show Password: shows password as you type
## ** modify to either 'True' or 'False' ** ###

verbose = True
show_password = True

### !! * ================ DO NOT MODIFY ANYTHING BELOW THIS ================ * !! ###

def cracking_process():
    import server
    import crack

    # step 1: get username and password
    global show_password
    user = server.prompt_id(show_password)

    # step 2: find the likelihood of the password's length
    global verbose
    crack.crack_length(user, verbose=verbose)


def clearConsole():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def help():
    print("To exit the program, type ':q'\n")


def main():
    clearConsole()
    print("Type in \'h\' for help in the username input")
    cracking_process()


if __name__ == "__main__":
    main()
