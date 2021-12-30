# import random
from getpass import getpass
import time
import string

def getAlpha() -> list:
    import os.path
    import csv

    characters = []

    # Get upper and lowercase letters
    if os.path.exists("alphabet.csv"):
        with open("alphabet.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                characters.append(row[0].upper())
                characters.append(row[0])
    elif os.path.exists("alphabet.xlsx"):
        try:
            __import__('pandas')
            __import__('openpyxl')
        except ImportError:
            pass
        else:
            import pandas as pd
            df = pd.DataFrame(pd.read_excel(open("alphabet.xlsx", 'rb')))
            for row in df['Letters']:
                characters.append(row.upper())
                characters.append(row)
    else:
        for char in string.ascii_letters:
            characters.append(char)

    return characters

def PasswordCracker():
    Run = True
    while Run:

        # * Preparation *
        # Included is a csv file of the alphabet in ranked order of most to least used in the English language
        # If file is absent, use traditional A-Z ordering - see README.md for more information
        characters = getAlpha()

        # Get all numbers (as strings) and symbols
        for char in range(0, 10):
            characters.append(str(char))

        # Change list into a tuple
        characters = tuple(characters)

        Try = True
        crackWord = ""
        idx = 0
        guessIdx = 0

        # * Preparation complete, get user password *
        # getpass hides user input
        password = getpass("Enter Your Password: ")

        if password == ":q":
            break

        if password == "h":
            help()
            while password == "h":
                password = getpass("Enter Your Password: ")        
        guessWord = tuple(password)
        
        # track how long it takes to crack the password
        startTime = time.perf_counter()
        while Try:

            char = guessWord[idx]
            guess = characters[guessIdx]

            if guess == char:
                idx += 1
                guessIdx = 0
                crackWord += char

                if idx >= len(guessWord):
                    endTime = time.perf_counter()
                    print()
                    print("Password Solved")
                    print(f"Password: {crackWord}")
                    print(f"It took {endTime - startTime} seconds to crack your password...\n")
                    Try = False
            else:
                guessIdx += 1

def help():
    print("To exit the program, type ':q'\n")

def main():
    print("Type in \'h\' for help")
    PasswordCracker()
    print("Exited Program Successfully.")

if __name__ == "__main__":
    main()