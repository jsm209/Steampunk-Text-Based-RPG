# Dice can roll hidden dice or ask for player involvement and roll a dice where they can see the outcome.
# The dice can have any number of sides anytime it is asked to be rolled.

import random


class Dice:

    # Pre: Given a value "sides" of type integer,
    # Post: Will ask for the player to push enter, roll a dice with the given sides, and return the result as an int.
    def roll(self, sides):
        input("[PRESS ENTER TO ROLL A " + str(sides) + " SIDED DICE] ")
        roll = random.randint(1, sides)
        if roll == 1 and sides == 20:
            print ("**You rolled a " + str(roll) + ". Say your prayers.**")
        elif roll == 20 and sides == 20:
            print ("**You rolled a " + str(roll) + "!! Don't get too excited.**")
        else:
            print ("**You rolled a " + str(roll) + "!**")
        return roll

    # Pre: Given a value "sides" of type integer,
    # Post: Will return a random int by rolling a dice with the given amount of sides.
    def hidden_roll(self, sides):
        roll = random.randint(1, sides)
        return roll

    # Pre: Given an integer that represents a lower limit of the roll, and an optional integer that represents the
    # upper limit,
    # Post: Fakes a d20 roll by intentionally tampering with the result. If you care about the result, use the regular
    # roll method instead. This is purely for flavor.
    def fake_roll(self, lowerlimit, upperlimit=20):
        input("[PRESS ENTER TO ROLL A " + str(20) + " SIDED DICE] ")
        roll = random.randint(lowerlimit, upperlimit)
        print("**You rolled a " + str(roll) + "!**")