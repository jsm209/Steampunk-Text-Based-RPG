from dice import *

# A player keeps track of important resources, and can display the amount of each resource they have.
# Additionally, the player has built in ways, such as mining, docking, and working, to gain more resources.

# POSSIBLE CHANGES (Using a dictionary instead of a list for the resources.)
# Make the resources into a dictionary, and make the given list in the add method a dictionary.
# Then change the add method to find the key with each corresponding resource name and add them that way..
# One reason not to do this is because dictionaries take up more memory, and it takes more work to create
# it each time, and I'm the only one implementing it so a list makes more sense..?


class Player:

    def __init__(self):
        self.resources = [0, 0, 0, 0, 100, 0, 0]
        self.resource_names = ["Credits", "Food", "Flux", "Hull", "Stress Level", "Crew", "Wisdom"]
        # Resources: Credits, Food, Fuel, Hull, Stress, Crew, Wisdom

    # Post: For each resource, outputs the name of the resource and the amount of the resource.
    # One special case is reporting stress, which is meant to be ambiguous, therefore lacking a clear value.
    def get_count(self):
        for x in range(0, 7):
            if x == 4:
                print(self.resource_names[x] + ": " + self.stress_status())
            else:
                print(self.resource_names[x] + ": " + str(self.resources[x]))

    # Post: Check the player's stress, and returns a value of type String, which is a purposely ambiguous description.
    def stress_status(self):
        if self.resources[4] <= 20:
            return "Almost insane"
        elif self.resources[4] <= 40:
            return "Dangerously stressed"
        elif self.resources[4] <= 60:
            return "Acutely stressed"
        elif self.resources[4] <= 80:
            return "Moderately stressed"
        else:
            return "Nervous"

    # Pre: Given a list containing exactly 7 values, where each index matches the index of the particular resource,
    # Post: Adds the resources, returning the resulting sum as a list.
    def add(self, other):
        if len(other) == 7:
            for x in range(0, 7):
                self.resources[x] += other[x]

    # Post: Presents dialogue to the player, where depending on a dice roll, determines the possible reward from
    # mining. A minimum of 4 Flux and 1 Crew will always be rewarded, with additional rewards depending on dice rolls.
    def mine(self):
        print("You take your airship towards the base of the closest isle.")
        print("The glimmering shine of the Flux stones can be seen through the roots\n"
              "that once held the landmass to the ground.")
        print("Taking your ship closer, you dock at the mining station and attempt to convince \n"
              "the mining crew foreman for permission to harvest Flux. He is a scruffy looking fellow,\n"
              "well built, and wears a sharp look on his face. Maybe you can convince him \n"
              "to lend you some of his workers as well.")
        d = Dice()
        check = d.roll(20)
        bonus = 0
        if check >= 15:
            print("'Ho there young lad! Looking to get flush? I admire your courage \n"
                  "to off The Maw, so I'll help you mine this here Flux on the fly!'")
            bonus += 2
        elif check >= 10:
            print("'Hmm lad, think you can in this day take Flux? There ain't a heap of it \n"
                  "left in Zernear, but I'll let ya have what I can give if it means ending The Maw.'")
            bonus += 1
        elif check >= 5:
            print("You scavengers are like Monkrats! Never ending supply of you lads I tell ya!\n"
                  "Flux is precious these days, take what you must but I tell ya it's scarce...'")
        else:
            print("'Hobble yer lip! You've got the hykey to ask for MY flux on MY mining rig?\n"
                  "I think ya got a screw loose. Good luck trying to get my workers to help.'")
            bonus -= 1
        print("You end up convincing the foreman to let you use his mine.")
        changes = [0, -d.hidden_roll(10), (4+bonus), 0, 0, (1+bonus), 0]
        print("The day is spent mining flux. The foreman's miners stare at you as you work, their curious\n"
              "gaze makes you feel slightly nervous. You can hear them whisper about you and The Maw. It seems\n"
              "that word must travel quickly on this mining rig.")
        print("You consume " + str(changes[1] * -1) + " food.")
        print("You end up mining " + str(changes[2]) + " Flux.")
        if changes[5] > 0:
            print("Also " + str(changes[5]) + " miner(s) opt to join you. You guess the life on the mining rig is boring.")
        self.add(changes)


p1 = Player()
p1.mine()
p1.get_count()

            

