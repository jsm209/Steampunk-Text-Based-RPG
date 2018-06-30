from dice import *

# Encounter lets you create encounters with a description, question, choice1, choice2, mod, and rating.
# An Encounter will reward the player if their check passes the rating.
# The player will always know their initial roll, but never the mod or rating for the Encounter.
# This way, even though the same encounter may occur more than once, they can have varying difficulties.
# You can set the win results and loss results, as well as the mod and rating with the following setters:
#
#   set_reward(self, text, reward):
#   Will deliver the given text upon winning, and return the given reward, which can later be added to their resources.
#   The reward must be in a list in the standard resource order: [Credits, Food, Fuel, Hull, Stress, Crew, Wisdom]
#
#   set_loss(self, text, punish):
#   Will deliver the given text upon losing, and return the given punish, which can later be added to their resources.
#   The reward must be in a list in the standard resource order: [Credits, Food, Fuel, Hull, Stress, Crew, Wisdom]
#
#   set_mod(self, mod):
#   Changes the Encounter's mod to the new given mod.
#
#   set_rating(self, rating):
#   Changes the Encounter's rating to the new given rating.
#
# Encounters will use this information to present the player with two choices, of which the mod will be
# applied when they choose choice1. The mod can be a positive or negative number, so choice1 won't always be good.
#
# get_outcome() will return a list with the appropriate resource changes, which can be added on to the player's
# resources. It will also print all the appropriate text as it works through the encounter.
#
# Process to create new encounters:
#   Create a new encounter object, feeding it the correct description, question, choice1, and choice2.
#   Set the encounter's reward and loss.
#   Set the encounter's rating (score to pass)
#   Set the encounter's mod (modifier to roll upon choosing choice1)



class Encounter:

    # Pre: Given a description, question, choice1, and choice2 of type String, where the description represents
    # the context of the encounter, the question represents the dilemma for the player, choice1 represents the decision
    # the mod will be applied to, and choice2 represents the decision without the mod,
    # Post: Will construct an Encounter with that data, that has no rewards or punishments, no win or loss text,
    # and a mod and rating value of 0.
    def __init__(self, description, question, choice1, choice2):
        self.description = description
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2

        self.win = ""
        self.reward = []
        self.lose = ""
        self.punish = []
        self.mod = 0
        self.rating = 0

    def __repr__(self):
        return 'New Encounter\nDescription=%s\nQuestion=%s\nWin=%s\n%s\nLose=%s\n%s\nMod=%s\nRating=%s' \
        % (self.description, self.question, self.win, self.reward, self.lose, self.punish, self.mod, self.rating)

    # Post: Will return a list of the the values of resources that was the outcome of the encounter.
    def get_outcome(self):
        print(self.description)
        choice = self.decision()
        d = Dice()
        check = d.roll(20)
        if choice == 1:
            check += self.mod
        if check >= self.rating:
            print(self.win)
            return self.reward
        else:
            print(self.lose)
            return self.punish

    # Post: Uses the encounter's choice1 and choice2 instance attributes to ask a question, returning 1 for choosing
    # choice1, and 2 for choosing choice2.
    def decision(self):
        print(self.question)
        print("Do you...")
        print("1: " + str(self.choice1))
        print("2: " + str(self.choice2))
        while True:
            choice = None
            try:
                choice = int(input("[ENTER 1 OR 2: ]"))
            except ValueError or choice not in range(1, 3):
                print("That isn't an option.")
                continue
            if choice in range(1, 3):
                return choice

    # Pre: Given text that represents the win message, and the reward, which is a list containing values to be added
    # to each player resource,
    # Post: Sets this encounter's win message and reward to the given values.
    def set_reward(self, text, reward):
        self.win = text
        self.reward = reward

    # Pre: Given text that represents the loss message, and the punishment, which is a list containing values to be
    # added to each player resource,
    # Post: Sets this encounter's loss message and punish to the given values.
    def set_loss(self, text, punish):
        self.lose = text
        self.punish = punish

    # Pre: Given an integer,
    # Post: Sets this encounter's mod value to the given value.
    def set_mod(self, mod):
        self.mod = mod

    # Pre: Given an integer,
    # Post: Sets this encounter's rating value to the given value.
    def set_rating(self, rating):
        self.rating = rating

d2 = Dice()

description = "This is my description."

question = "Which do you choose?"

choice1 = "Choice1"
choice2 = "Choice2"

e = Encounter(description, question, choice1, choice2)
e.set_mod(-3)
e.set_rating(10)
e.set_reward("Your investigation suceeded.",
             [0, -d2.hidden_roll(3), 0, 0, -5, -d2.hidden_roll(3), 2 + d2.hidden_roll(3)])

e.set_loss("Your investigation failed.",
           [0, -d2.hidden_roll(3), 0, 0, -5, -d2.hidden_roll(3), 2 + d2.hidden_roll(3)])

print(e)

# hmm = e.get_outcome()

# Resources: Credits, Food, Fuel, Hull, Stress, Crew, Wisdom
