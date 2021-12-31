# Password Cracker
This is a tweaked program demonstrating how a timed attack password cracker work. [The Server](#the-server) is a simple input that gets the user's username and password, and then stores it into a dictionary.

## "The Server"
This program does **NOT** accurately model how passwords are cracked and how they are passwords are stored. Instead, this program uses the most simplified process of how passwords are stored. Many servers are secured and use encryption to store passwords in a much more secured way. Most servers also only allow a few number of tries before blocking the user out for fraud or spam attempts, so this program won't work for most secured servers.

This program only demonstrates at a shallow level the process of password cracking and the emphasize the importance of a secure password. 

# How It Works
## Setup
1. The program first prompts the user to enter a username and password.
2. The program stores them as a key:value dict item into a dictionary container.

## Prepping
3. The program finds the maximum likelihood of the user's password of being length L. This reduces the the time exponentially since the program can target passwords of only length L.

## Cracking
4. The program runs a timed attack on the server and attempts to find a set of characters that the password could be. Correct characters will take longer for the server to respond incorrect to, so slowly deduce each character until the full password is cracked.


# Future Plans
I plan on implementing a webpage version of this program so that a Python compiler is not needed to run this. I also plan on adding a file feature; where the program can take in a file of passwords and crack each password.

Along with it, I plan on adding more features. One such feature in mind is allowing the user to input N "previous users" into the password database. Currently, the program initializes an password database. This stores all of the usernames and passowrds as a dictionary. Since it is empty, it will obviously be faster to crack your password. This feature will allow the user to insert N computer-generated usernames with corresponding random passwords into the database.

However, as of 2021-12-29 (Dec 29), I currently do not have the knowledge to implement such a software yet.