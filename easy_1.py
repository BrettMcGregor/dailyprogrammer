# create a program that will ask the users name, age, and reddit username.
# have it tell them the information back, in the format:
#
# your name is (blank), you are (blank) years old, and your username is (blank)
#
# for extra credit, have the program log this information in a file to be accessed later.

name = input("Please enter your name: ")
age = input("Please enter your age: ")
username = input("Please enter your Reddit username: ")

with open("details.txt", "w") as file:
    file.write("name, age, username\n")
    file.write(f"{name}, {age}, {username}\n")

print(f"Your name is {name}, you are {age} years old, and your username is {username}")
print("Data saved to 'details.txt'")
