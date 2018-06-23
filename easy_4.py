# You're challenge for today is to create a random password generator!
#
# For extra credit, allow the user to specify the amount of passwords to generate.
#
# For even more extra credit, allow the user to specify the length of the strings he wants to generate!

import string
import random


def password_generator(num, length):
    passwords = []
    characters = [x for x in string.ascii_letters]
    for char in string.digits:
        characters.append(char)
    for i in range(num):
        password = ""
        for j in range(length):
            password += random.choice(characters)
        passwords.append(password)
    return passwords


print(password_generator(int(input("Enter number of passwords: ")), int(input("Enter length: "))))
