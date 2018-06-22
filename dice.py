import random


class Dice:

    def roll(self, sides):
        roll = random.randint(1, sides)
        if roll == 1 and sides == 20:
            print ("You rolled a " + str(roll) + ". Say your prayers.")
        elif roll == 20 and sides == 20:
            print ("You rolled a " + str(roll) + "!! Don't get too excited. ")
        else:
            print ("You rolled a " + str(roll) + "! ")
        return roll