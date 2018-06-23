# Your challenge for today is to create a program which
#  is password protected, and wont open unless the correct
#  user and password is given.
#
# For extra credit, have the user and password in a separate .txt file.
#
# for even more extra credit, break into your own program :)


def create_user():
    username = input("Please enter your new username: ")
    password = input("Please enter your new password: ")
    with open("credentials.txt", "w") as file:
        file.write(f"{username}\n")
        file.write(f"{password}\n")


def login():
    with open("credentials.txt") as file:
        right_username = file.readline().strip("\n")
        right_password = file.readline().strip("\n")
        while True:
            username = input("Username: ")
            password = input("Password: ")
            if username == right_username and password == right_password:
                print("Access Granted.")
                break
            else:
                print("Access Denied.\n")


# create_user()
login()
