# Write a program that prints a string from a list at random,
# expects input, checks for a right or wrong answer, and keeps
# doing it until the user types "exit". If given the right
# answer for the string printed, it will print another and
# continue on. If the answer is wrong, the correct answer is
# printed and the program continues.
#
# Bonus: Instead of defining the values in the program, the
# questions/answers is in a file, formatted for easy parsing.
#
# Example file:
# 12 * 12?,144
# What is reddit?,website with cats
#     Translate: hola,hello

import csv
import random


def get_question(f):
    with open(f"{f}") as file:
        next(file)
        contents = [x for x in csv.reader(file)]
        question, answer = random.choice(contents)
        return question, answer


def main_loop():
    while True:
        question, answer = get_question("easy_33.txt")
        user_answer = input(f"Please answer the following question\nQ.{question}\n> ")
        if user_answer.upper() == "EXIT":
            print("Exiting program.")
            break
        elif user_answer == answer:
            print("Correct!")
            continue
        else:
            print(f"Incorrect. The answer was {answer}.")
            continue


main_loop()
