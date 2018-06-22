# we all know the classic "guessing game" with higher or lower
# prompts. lets do a role reversal; you create a program
# that will guess numbers between 1-100, and respond appropriately
# based on whether users say that the number is too high or too low.
# Try to make a program that can guess your number based on user
# input and great code!

low = 0
high = 101
guess = int((high - low) / 2)

while True:
    print(f"My guess is {guess}\n"
          f"Let me know if your number is (H)igher or (L)ower or (C)orrect.")
    feedback = input("> ")
    if feedback.upper() == "C":
        print(f"Great! I guessed your number. It was {guess}")
        break
    elif feedback.upper() == "H":
        low = guess
        guess += int((high - low) / 2)
    elif feedback.upper() == "L":
        high = guess
        guess -= int((high - low) / 2)
    else:
        print("Enter H,L or C")
