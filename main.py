# Verbose: shows some statistics, dialouge, and the cracker working its magic
# Show Password: shows password as you type
## ** modify to either 'True' or 'False' ** ###

verbose = True
show_password = False

### !! * ================ DO NOT MODIFY ANYTHING BELOW THIS ================ * !! ###

def cracking_process():
    import server
    import crack

    # step 1: get username and password
    global show_password
    user = server.prompt_id(show_password)

    # step 2: find the likelihood of the password's length
    global verbose
    length = crack.crack_length(user, verbose=verbose)

    # dialogue
    print(f"Using most likely length: {length}\n")
    input("Hit enter to continue...")

    # step 3: crack the password
    password, startTime = crack.crack_password(user, length, verbose=verbose)

    # dialogue
    import time
    import numpy as np
    
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    print(f'\nPassword cracked: {password}')
    print(f'It took {elapsedTime:.4f} seconds long to crack it...')


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
