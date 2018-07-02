import time

#############
# CONSTANTS #
#############

# Tracks the amount of progress the player made.
TURN = 1

# Base list of valid actions
VALID_ACTIONS = ["walk forward", "walk backward", "examine", "inventory", "status", "mood"]

# Additional actions added over time
ADD_ACTIONS = []


# Post: Presents an introduction
# Give opening text
def opening_story():


# Gets a random entry from the list
def random_list_entry():


# Advances the turn counter by 1
def next_turn(self):
    global TURN
    self.TURN += 1

def single_player_game(self, player):
    global TURN
    while TURN <= 20:
        # "It is the start of day X. You check your resources:"
        # call player's status method.
        # ask the player what action they want to perform.
        # if it is not an encounter, call the player's mine, work, dock method.
        # if it is an encounter, get a random list entry from the appropriate list of encounters depending if
        #   the player chose research or exploration
        # At the end of the turn, advance the counter by 1.




# Pre: Given a valid integer.
# Post: Will walk that far in the positive or negative direction as long as the total steps is greater than 0.
def walk(num):
    global TURN
    if TURN + num < 1:
        print("You quickly bump into a wall.")
    else:
        TURN += num


# Pre: Given a list of possible actions, and an additional list of extra actions,
# Post: Will collect input from the player and execute their selected action.
def action_exploration(actions, extra=[]):
    print("Looking around, you realize you have a number of options.")
    time.sleep(1)
    print("You can: ")
    time.sleep(1)
    for x in actions + extra:
        print("    " + x)
    indecisive = True
    # check if decision is legal, and if so do that action. If not then try again.
    while indecisive:
        decision = input("What do you do? ").lower()
        if decision in actions + extra:
            output = "You "
            if decision == "walk forward":
                output = output + decision + "."
                walk(1)
            elif decision == "walk backward":
                print("You walk backward.")
                walk(-1)
            elif decision == "examine":
                print("You take a look around.")
                global ADD_ACTIONS
                ADD_ACTIONS = examine()
            elif decision == "inventory":
                # call list of items
                print("You rummage through your bag.")
            elif decision == "status":
                # call player's stats and condition
                print("You take a deep breathe.")
            elif decision == "mood":
                # call mood
                print("You're feeling moody")
            time.sleep(4)
            indecisive = False
        else:
            print("I can't comprehend that.")


# Given
def examine():
    global TURN
    add_actions = []
    if TURN == 1:
        print("You're in a cave with a pool of water in the center of the room.")
        print("Upon close examination, you see a wrench in the wreckage pile.")
        add_actions = ["pick up wrench"]
    elif TURN == 2:
        print("You're on a cliff overlooking a valley of clouds.")
    elif TURN == 3:
        print("There are scattered mechanical parts and.. uh.")
    return add_actions


def storyline():
    global TURN
    opening_story()
    while TURN <= 10:
        print("Your TURNS is " + str(TURN))
        action_exploration(VALID_ACTIONS, examine())


# Get a method that creates encounter objects from a text file, and adds them to a list while there is still text.
def build_encounters(file):
    encounters = []
    infile = file(file, "r")
    # line = infile.readLine()
    while infile != "" :
        # Store basic parameters for an encounter
        description = ""
        encounter = ""
        win = ""
        lose = ""
        mod = 0
        rating = 10
        if infile.readLine() == "description:":
            while infile.readLine() != "question:":
                description = description + infile.readLine()
        elif infile.readLine() == "encounter":
            while infile.readLine() != "win:":
                encounter = encounter + infile.readLine()
        elif infile.readLine() == "win:":
            while infile.readLine() != "reward:":
                win = win + infile.readLine()
        elif infile.readLine() == "reward:":
            # put the following seven numbers into a list.
        elif infile.readLine() == "lose:":
            while infile.readLine() != "punish:":
                lose = lose + infile.readLine()
        elif infile.readLine() == "punish:":
            # put the following seven numbers into a list.
        elif infile.readLine() == "mod:":
            mod = infile.readLine()
        elif infile.readLine() == "rating:":
            rating = infile.readLine()
        else:
            raise Exception("Given file not in correct format.")
            return null
        # Things to test:
            # Does reading lines of text actually store it correctly in the encounter?
            # Does creating new lines in the text file translate correctly to encounter?

        # TODO:
            # Find a way to parse text into a list.
            # Actually import the encounter class and build the encounter, then test it using the _repr_ command.





