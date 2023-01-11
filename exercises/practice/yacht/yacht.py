# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category == ONES:
        return dice.count(1)

    if category == TWOS:
        return dice.count(2) * 2

    if category == THREES:
        return dice.count(3) * 3

    if category == FOURS:
        return dice.count(4) * 4

    if category == FIVES:
        return dice.count(5) * 5

    if category == SIXES:
        return dice.count(6) * 6

    if category == FULL_HOUSE:
        if len(set(dice)) == 2 and ( dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return sum(dice)
        else:
            return 0

    if category == FOUR_OF_A_KIND:
        if dice.count( max(set(dice), key = dice.count) ) >= 4:
            return max(set(dice), key = dice.count) * 4
        else:
            return 0

    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1,2,3,4,5]:
            return 30
        else:
            return 0

    if category == BIG_STRAIGHT:
        if sorted(dice) == [2,3,4,5,6]:
            return 30
        else:
            return 0

    if category == CHOICE:
        return sum(dice)
