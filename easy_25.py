# In an election, the person with the majority
# of the votes is the winner. Sometimes due to
# similar number of votes, there are no winners.
#
# Your challenge is to write a program that determines
# the winner of a vote, or shows that there are no
# winners due to a lack of majority.


def election(votes):
    d = [[x, 0] for x in set(votes)]
    for i in range(len(set(votes))):
        count = 0
        for vote in votes:
            if d[i][0] == vote:
                count += 1
        d[i][1] = count
    d = sorted(d, key=lambda x: x[1], reverse=True)
    if d[0][1] != d[1][1]:
        return f"Winner is '{d[0][0]}'."
    return f"No majority."


print(election(['A', 'A', 'A', 'C', 'C', 'B', 'B', 'C', 'C', 'C', 'B', 'C', 'C']))
