# create a program that will allow you to enter events organizable by hour.
# There must be menu options of some form, and you must be able to easily edit,
#  add, and delete events without directly changing the source code.
#
# (note that by menu i don't necessarily mean gui. as long as you can easily
# access the different options and receive prompts and instructions telling
# you how to use the program, it will probably be fine)

import csv
import os

print(f"\n{'Event Manager':*^66}")

events = []  # list to store the event records

if os.path.isfile("event_manager.txt"):
    with open("event_manager.txt", newline="") as file:  # if file exists. Store existing data in a list
        next(file)  # skip the header row
        data = csv.reader(file)
        for line in data:
            events.append(line)
else:
    with open("event_manager.txt", "a") as file:  # if file does not exist. create and write header row
        pass

try:
    new_event_unique_id = int(max(x[0] for x in events))  # get the last unique_id

except ValueError:
    new_event_unique_id = 0
except IndexError:
    new_event_unique_id = 0

while True:
    raw_input = input("(A)dd new event, (R)emove event, (D)isplay events, (Q)uit program.\n> ")

    if raw_input.upper() == "Q":
        with open("event_manager.txt", "w") as file:
            file.write("id,time,details\n")
            for row in events:
                file.write(f"{row[0]},{row[1]},{row[2]}\n")
        break

    elif raw_input.upper() == "A":
        new_event_unique_id += 1
        new_event_time = input("Please enter the event time (e.g. 1400).\n> ")  # could implement date as well
        new_event_details = input("Please enter the event details.\n> ")
        events.append([new_event_unique_id, new_event_time, new_event_details])

    elif raw_input.upper() == "D":
        events = sorted(events, key=lambda time: int(time[1]))
        print(f"{'id':<3}{'time':>4} {'details':<20}")
        for row in events:
            print(f"{row[0]:<3}{row[1]:>4} {row[2]:<20}")
        print()

    elif raw_input.upper() == "R":
        events = sorted(events, key=lambda time: int(time[1]))
        print(f"{'id':<3}{'time':>4} {'details':<20}")
        for row in events:
            print(f"{row[0]:<3}{row[1]:>4} {row[2]:<20}")
        print()

        remove = input("Please enter the id of the event you wish to remove.\n> ")
        for row in events:
            if row[0] == remove:
                events.remove(row)

        events = sorted(events, key=lambda time: int(time[1]))
        print(f"{'id':<3}{'time':>4} {'details':<20}")
        for row in events:
            print(f"{row[0]:<3}{row[1]:>4} {row[2]:<20}")
        print()











