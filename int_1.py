# create a program that will allow you to enter events organizable by hour.
# There must be menu options of some form, and you must be able to easily edit,
#  add, and delete events without directly changing the source code.
#
# (note that by menu i don't necessarily mean gui. as long as you can easily
# access the different options and receive prompts and instructions telling
# you how to use the program, it will probably be fine)

import os
import csv


def display_events():
    event_list = sorted(events, key=lambda time: int(time[1]))
    print(f"{'id':<3}{'time':>4} {'details':<20}")
    for r in event_list:
        print(f"{r[0]:<3}{r[1]:>4} {r[2]:<20}")
    print()


def add_event():
    try:
        event_id = int(max(x[0] for x in events))  # get the last unique_id
    except ValueError:
        event_id = 0
    except IndexError:
        event_id = 0
    event_id += 1
    new_event_time = input("Please enter the event time (e.g. 1400).\n> ")  # could implement date as well
    new_event_details = input("Please enter the event details.\n> ")
    events.append([event_id, new_event_time, new_event_details])
    return events


def remove_event():
    remove = int(input("Please enter the id of the event you wish to remove.\n> "))
    for row in events:
        if row[0] == remove:
            events.remove(row)
            print(f"Event {row[0]} removed")
    return events


def quit_program():
    with open("event_manager.txt", "w") as file:
        file.write("id,time,details\n")
        for row in sorted(events, key=lambda time: int(time[1])):
            file.write(f"{row[0]},{row[1]},{row[2]}\n")


print(f"\n{'Event Manager':*^66}")

events = []  # list to store the event records

if os.path.isfile("event_manager.txt"):
    with open("event_manager.txt", newline="") as file:  # if file exists. Store existing data in a list
        next(file)  # skip the header row
        for x, y, z in csv.reader(file):
            events.append([int(x), y, z])
else:
    with open("event_manager.txt", "a") as file:  # if file does not exist. create and write header row
        pass

while True:
    raw_input = input("(A)dd new event, (R)emove event, (D)isplay events, (Q)uit program.\n> ")
    if raw_input.upper() == "Q":
        quit_program()
        break
    elif raw_input.upper() == "A":
        add_event()
    elif raw_input.upper() == "D":
        display_events()
    elif raw_input.upper() == "R":
        display_events()
        remove_event()



