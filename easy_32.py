# lets simulate a roulette wheel!
# a program that takes as input your bet, and gives
# as output how much you won, with the appropriate probability
#
# write a program that will take a players bet and output
# the resulting spin and payout. try using an american
# roulette wheel (which has the 00 slot) to add a slight twist.
# and try to incorporate as many complex bets as you can to.
# a comprehensive list can be found here

import random
import os


def roulette():
    game_dict = [['1', '0', 35], ['2', '00', 35], ['3', 'Straight up', 35], ['4', 'Row', 17],
                ['5', 'Split', 17], ['6', 'Street', 11], ['7', 'Corner', 8],
                ['8', 'Top line(US)', 6], ['9', 'Top line(European)', 8],
                ['10', 'Six line', 5], ['11', '1st column', 2], ['12', '2nd column', 2],
                ['13', '3rd column', 2], ['14', '1st dozen', 2], ['15', '2nd dozen', 2],
                ['16', '3rd dozen', 2], ['17', 'Odd', 1], ['18', 'Even', 1], ['19', 'Red', 1],
                ['20', 'Black', 1], ['21', '1 to 18', 1], ['22', '19 to 36', 1]]
    # try:
    if os.path.isfile("player_balance.txt"):
        with open("player_balance.txt") as file:
            player_balance = int(file.readline())
    else:
        player_balance = 100

    # TODO: prompt user for bet amount and type

    while True:
        # print("\n" * 40)
        print(f"{'id':<4}{'pays':<5}{'bet name':<20}")
        for bet in game_dict[:3]:
            print(f"{bet[0]:<4}{bet[2]:<5}{bet[1]:<20}")
        bet_type = input("\nPlease select bet type: ")
        # TODO: prompt user for more information based on bet type e.g. which six-line?
        numbers = []
        if bet_type == '1':
            numbers = ['0']
        elif bet_type == '2':
            numbers = ['00']
        elif bet_type == '3':
            while True:
                numbers = input("Please select number for your bet 1-36> ")
                if 1 <= int(numbers) <= 36:
                    break
                else:
                    print("Outside range. Try again.")

        while True:
            bet_amount = int(input(f"Your bank balance is ${player_balance}.\nPlease enter bet amount: $"))
            if bet_amount < player_balance:
                break
            else:
                print("You dont have that much cash!")


        # TODO: use random to generate spin result
        # TODO: ask player for French or American style. Implement based on user choice e.g. 00 in American
        # TODO: keep player cash total

        wheel = [0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]  # TODO: use a range() generator expression but what about 00
        # wheel = [x for x in range(37)]
        

        result = f"The wheel has spun and the number is... {random.choice(wheel)}!"
        print(result)
        print(numbers)
        if result in numbers:
            payout_value = int(bet_amount) * game_dict[int(bet_type)-1][2]
            print(f"Congratulations. You win ${payout_value}")
            player_balance += payout_value
        else:
            print("Sorry you lose.")
            player_balance -= int(bet_amount)
        with open("player_balance.txt", "w") as file:
            file.write(str(player_balance))
        print(f"Player now has ${player_balance}")

        replay = input("Play again? (Y/n) ")
        if replay.upper() == "Y":
            continue
        else:
            break


roulette()
