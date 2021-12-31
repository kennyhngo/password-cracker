import time
import string
import math

# def getAlpha() -> list:
#     import os.path
#     import csv

#     characters = []

#     # Get upper and lowercase letters
#     if os.path.exists("alphabet.csv"):
#         with open("alphabet.csv") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 characters.append(row[0].upper())
#                 characters.append(row[0])
#     elif os.path.exists("alphabet.xlsx"):
#         try:
#             __import__('pandas')
#             __import__('openpyxl')
#         except ImportError:
#             pass
#         else:
#             import pandas as pd
#             df = pd.DataFrame(pd.read_excel(open("alphabet.xlsx", 'rb')))
#             for row in df['Letters']:
#                 characters.append(row.upper())
#                 characters.append(row)
#     else:
#         for char in string.ascii_letters:
#             characters.append(char)

#     return characters


# def setUp():
#     Run = True
#     while Run:

#         # * Preparation *
#         # Included is a csv file of the alphabet in ranked order of most to least used in the English language
#         # If file is absent, use traditional A-Z ordering - see README.md for more information
#         characters = getAlpha()

#         # Get all numbers (as strings) and symbols
#         for char in range(0, 10):
#             characters.append(str(char))

#         # Change list into a tuple
#         characters = tuple(characters)

#         # * Preparation complete, get user password *
#         # getpass hides user input
#         password = getpass("Enter Your Password: ")

#         if password == ":q":
#             break

#         if password == "h":
#             help()
#             while password == "h":
#                 password = getpass("Enter Your Password: ")     
#         password = list(password)

#         CrackPassword(password, characters)


# def CrackPassword(password, characters):
    
#     Run = True
#     guess = characters[0] * len(password)
#     guess = list(guess)
#     print(password)

#     # track how long it takes to crack the password
#     startTime = time.perf_counter()

#     guess_idx = 1
#     char_idx = 1
#     len_char = len(characters)

#     while Run:
#         for char in characters:

#             guess[0] = char
#             displayTime(startTime)

#             if guess == password:
#                 displayPassword(guess, startTime)
        
#         guess[guess_idx] = characters[char_idx]
#         char_idx += 1

#         if char_idx == len_char - 1:
#             guess_idx += 1
#             char_idx = 1



# function to tell user how long the program has been running
# def displayTime(startTime):
#     midTime = time.perf_counter()
#     Time = midTime - startTime
#     if (math.floor(Time) > 0):
#         if math.floor(Time) % 10 == 0:
#             print(f"{midTime - startTime} seconds elapsed...")


def crack_length(user, max_password_length=32, verbose=False) -> int:
    import numpy as np
    import timeit

    trials = 1000
    attempts = np.empty(max_password_length)

    for i in range(max_password_length):
        i_time = timeit.repeat(stmt='check_password(user, x)',
                               setup=f'user={user!r};x=random_str({i!r})',
                               globals=globals(),
                               number=trials,
                               repeat=10)
        # repeat the function check_password(user, x)
        # with user parameter given user=user and x is a random string of length i
        # gloals() gives access to global variables
        # do this process trials=1000 amount of times
        # repeat above repeat=10 amount of times 

        attempts[i] = min(i_time)
        # take the minimum time for lowest variablility

        if verbose:
            most_likely_length = np.argsort(attempts[::-1][:5])
            print(most_likely_length, attempts[most_likely_length] / attempts[most_likely_length[0]])
            # top 5 most likely password lengths as a percentage of the first most likely length
                # as a percentage of the first

        most_likely = int(np.argmax(attempts))
        return most_likely
