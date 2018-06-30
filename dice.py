import random

# Dice can roll hidden dice or ask for player involvement and roll a dice where they can see the outcome.
# The dice can have any number of sides anytime it is asked to be rolled.


class Dice:

    # Pre: Given a value "sides" of type integer,
    # Post: Will ask for the player to push enter, roll a dice with the given sides, and return the result as an int.
    def roll(self, sides):
        input("[PRESS ENTER TO ROLL]")
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