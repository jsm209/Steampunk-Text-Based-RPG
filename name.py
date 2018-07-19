import random


# A Name is capable of generating a random name, that has the option to include a last name and/or a title.
class Name:

    def __init__(self):
        self.suffix = ["Cryptographer", "Professor", "Analog", "Foreman", "Pirate", "Councilor", "Priest", "Assassin",
                       "Mechanic", "Doctor", "Miner", "Spy", "Banker", "Mortician", "Caretaker", "Foolish", "Baron",
                       "Chancellor", "Inventor", "Scientist", "Cultist", "Ambidextrous", "Ambitious", "Liar", "Thief",
                       "Murderer", "Gravedigger", "Aviator", "Hunter", "Soldier", "Elderly", "Disabled"]
        self.first_names = ["Bram", "Hugo", "Edison", "Ida", "Agatha", "Ives", "Briar", "Phineas", "Sterling", "Tesla", "Victoria",
                            "Emily", "Edna", "Ellie", "Ruth", "Bess", "Fanny", "Theodore", "Alethea", "Anastasia", "Bertram",
                            "Ambrose", "Pierce", "Percy", "Conrad", "Maximilian", "Alistar"]
        self.last_names = ["Rockwell", "Mortimer", "Sheffield", "Blackwood", "Hopkins", "Cogsworth", "Hollingsworth",
                           "Babbage", "Bishop", "Jefferson", "Arkham", "Whitley", "Wallace", "Mordecai"]

    # Pre: Given two booleans, first whether or not to include a last name, and second whether to include a title,
    # Post: Returns a string that is a random name.
    def generate_name(self, last = True, title = False):
        firstname = random.choice(self.first_names)
        lastname = random.choice(self.last_names)
        suffix = random.choice(self.suffix)

        name = firstname
        if last is True:
            name += " " + lastname
        if title is True:
            name += " the " + suffix
        return name

    def generate_suffix(self):
        return random.choice(self.suffix)
