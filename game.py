from dice import *
from encounter import *
from encounterGroup import *
from player import *

TURN = 1  # Tracks the amount of progress the player made.
d = Dice()  # A dice to share with all the game mechanics.


# Post: Presents an introduction
def opening_story():
    print("Opening story.")


# Post: Advances the turn counter by 1
def next_turn():
    global TURN
    TURN += 1

# Pre: Given a player object,
# Post: Will carry out all the processes necessary for a single player game of Lugmere's Loss. It presents the initial
# story, and processes 20 turns before presenting a final encounter.
def single_player_game(player):
    global TURN
    while TURN <= 20:
        # "It is the start of day X. You check your resources:"
        # call player's status method.
        # ask the player what action they want to perform.
        # if it is not an encounter, call the player's mine, work, dock method.
        # if it is an encounter, get a random list entry from the appropriate list of encounters depending if
        #   the player chose research or exploration
        # At the end of the turn, advance the counter by 1.
        print()
        print("It is the start of day " + str(TURN) + ". You have: ")
        print()
        p1.get_count()
        print()
        print("How do you spend your day?")

        process_turn(player)
        next_turn()
        # After 20 turns, encounter The Maw.


# Post: Presents the user with 5 courses of action, and returns a valid integer 1-5 that represents the chosen action.
def action_prompt():
    print("Do you...")
    print("1: Mine")
    print("2: Dock")
    print("3: Work")
    print("4: Research")
    print("5: Explore")
    while True:
        choice = None
        try:
            choice = int(input("[ENTER ANY NUMBER 1-5: ]" ))
        except ValueError or choice not in range(1, 6):
            print("That isn't an option.")
            continue
        if choice in range(1, 6):
            return choice


# Pre: Given a valid player object,
# Post: Processes one full turn for the player. After getting a course of action from the player, it performs it
# assuming the player has the resources to do so. If the action was not able to be performed (due to a lack of
# resources) it asks the player again for a different decision.
def process_turn(player):
    choice = action_prompt()
    if choice == 1:
        player.mine(d)
    elif choice == 2 and player.resources[0] >= 100:
        player.dock(d)
    elif choice == 3:
        player.work(d)
    elif choice == 4 and player.resources[5] > 0 and player.resources[2] > 0:
        player.resources[2] -= 1
        player.resources[5] -= 1
        encounter = research_encounters.get_random_encounter()
        player.add(encounter.get_outcome())
    elif choice == 5:
        print("PLACEHOLDER, PLAYER EXPLORES.")
    else:
        print("You don't have the resources to do that. Please select another course of action.")
        process_turn(player)

##############
# ENCOUNTERS #
##############

# General Notes:
#   The content below contains 20 encounters, the first 10 are research encounters, and the last 10 are exploration
#   encounters.
#
#   Encounter() constructor parameters are in the following order:
#   description, choice1, choice2, win message, win resources, lose message, lose resourced, mod, rating
#
#   The reward must be in a list in the standard resource order:
#   [Credits, Food, Fuel, Hull, Stress, Crew, Wisdom]


# RESEARCH ENCOUNTERS:
research_encounters = encounterGroup()
research_encounters.add(Encounter(
    "Your uncle, a prosperous Flux mining rig foreman used to help fund the research of Dr. Stynbeck, an alienist by\n"
    "trade and a leading expert on research about The Maw. Both he and your uncle mysteriously disappeared 9 years\n"
    "ago, and are believed to be dead. However neither of their bodies were found and both of their homes fell victim\n"
    "to an unknown arsonist. One of the few heirlooms from your uncle that you inherited was a journal containing \n"
    "broken clues about their research. One of the entries contains the whereabouts of Dr. Stynbeck's hidden library,\n"
    "and your uncle's abandoned Flux mining rig. You can only spend the day investigating either location, but not \n"
    "both. Which do you choose?",
    "Dr. Stynbeck's Library",
    "Your Uncle's Mining Rig",
    "Your investigation proves fruitful, and you're enlightened with more knowledge about The Maw. You learn that \n"
    "The Maw has a cult following, and it is these individuals who destroyed much of the original research. Just as \n"
    "you realize this, you feel another presence nearby, and turn to look only to see a hooded figure quickly duck \n"
    "out of view... You fail to locate the mysterious figure.",
    [0, -1, 0, 0, 1*d.hidden_roll(4), -2, 2],
    "Your investigation failed.",
    [0, -1, 0, 0, 1*d.hidden_roll(4), -1, 0],
    3,
    10
))

research_encounters.add(Encounter(
    '''
    While traveling to your next destination, an unusual amount of fog engulfs your airship.  The color is a tinge of
    dark green, which you find unusual compared to the smog that covers Lugmere. An eerie silence falls over you and
    your crew, as you all stare at each other, unsure of where you're are, where you're going, and strangely, where
    you just came from. In fact, it is hard to recall anything, even your own name, and you stare helplessly at the
    skies, not sure about anything. Shuffling can be heard, and you soon see mite like creatures with oily bodies
    crawl up the side of your vessel and onto the deck. You have free will, yet you don't feel inclined to warn your
    crew mates about the creatures crawling up their legs. You can see them excreting a dark green gas, strikingly
    similar to the clouds that surround the airship. Tens of these creatures slither across the deck, and one arrives
    at your feet, crawling up your leg. It engulfs your head, and your thoughts are soon whisked away to another realm.
    ''',
    "Embrace your mind",
    "Rip the mite off",
    '''
    You gain control of your thoughts, and you're filled with spatial understanding beyond this world. You can see
    yourself, standing on the tiny airship floating among the clouds. Further out, it looks like the entirety of Lugmere
    could fit in your palm. Your eyes peer downwards to see a massive worm-like creature, its mouth at the base of
    the city. Beneath the mouth is a mess of swirling coils of scales, fur, and indescribable appendages. Just then,
    you see an electrical surge flow through its body as it howls, and Lugmere lights up more ever so slightly.
    Your vision fades as you succumb to fatigue and drowsiness...
    You soon wake up to find yourself enlightened, and your airship untouched and safe. You're not sure if your crew
    also experienced the same, but you note the experience and continue as if it didn't happen.
    ''',
    [0, 0, 0, 0, -5*d.hidden_roll(2), -2, 2],
    '''
    You fail to meld with the creature, and you succumb to its gas. You wake to find your airship lodged into a random
    island, crew members are missing, and the early morning sun casting its light onto your face. Without a clue as to
    how long you were unconscious, you continue on your way, noting this encounter with the strange mite. 
    
    ''',
    [0, 0, 0, -2, -5*d.hidden_roll(4), -1*d.hidden_roll(2), 1],
    12,
    25
))

research_encounters.add(Encounter(
    '''
    One suspicion you've had with your dream about being swallowed by The Maw is that if you had not woken up early,
    perhaps you could have seen inside the horror herself, and understood more about the terror. Intrigued by this idea,
    you set out to explore dream and vision inducing drugs and ingredients. Your efforts have not gone unnoticed
    however, and eventually a strange woman approaches you in the night. She is dressed in a robe that bears the 
    insignia of \"The Mawful\", a cult that worships The Maw. She hands you a strange mushroom, and tells you that
    ingesting it provokes strong dreams and visions. However, she explains that the plant has to be dissolved in a 
    concoction made from the blood and heart of a human, spelling death for whoever is chosen for such a sacrifice.
    You figure you can make a similar concoction with an animal rather than a human. What do you do?
    ''',
    "Sacrifice one crew member",
    "Sacrifice an animal",
    '''
    Your mixture works, and you have a vivid dream about The Maw. You drift around the creature, and observe that it
    has a worm-like body with limbs that stretch all the way to the center of the world. You're able to count 18 
    distinct limbs whose length tangles with other limbs, producing a sea of snake like appendages. You realize Lugmere 
    is a mere tip of a needle in comparison to the size of the beast, and you are frightened as you awake, again in a
    pool of your own sweat.
    ''',
    [0, -1, 0, 0, -5, -1, 3],
    '''
    Your mixture fails. Perhaps the concoction wasn't made correctly, or maybe the mysterious plant was not to be
    trusted, but either way you feel horrible. Instead, you have a nightmare, and feel the wrath of The Maw as she 
    tears you apart. She harshly whispers to you in an unknown tongue, syllables piercing your brain. You awake on the
    floor, and your room is trashed. Your stomach is on fire and you have a terrible fever, but you push
    yourself to keep going, because the window to solve Lugmere's problem is quickly closing.

    ''',
    [0, -1, 0, 0, -15, -1 * d.hidden_roll(2), 1],
    3,
    13
))


# Starts a game of Lugmere's Loss.
p1 = Player()
single_player_game(p1)





