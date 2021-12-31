def cracking_process():
    import server
    import crack

    # step 1: get username and password
    server.prompt_id()

    # step 2: find the likelihood of the password's length
    crack.crack_length()

def clearConsole():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def help():
    print("To exit the program, type ':q'\n")
    print("I would recommend trying small password inputs - like 2 or 3 characters long.\n" +
          "And if you have time, try a password that's 4-6 characters long and let it run\n" +
          "in the background. And check back on it every once in a while.\n")


def main():
    clearConsole()
    print("Type in \'h\' for help or more information")
    print("I would limit the input to 7 characters max to avoid long computation time.\n")

    cracking_process()
    print("Exited Program Successfully.")


if __name__ == "__main__":
    main()
