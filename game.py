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
def opening_story():
    print("You slowly come to your senses as you wake up in a pool of water.")
    time.sleep(5)
    print("Moss, scattered nuts and bolts, and patches of dead grass surround your pool.")
    time.sleep(5)
    print("You soon come to realize you're in a cave, and light peers in from an opening.")
    time.sleep(5)
    print("...")
    time.sleep(5)


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


storyline()




