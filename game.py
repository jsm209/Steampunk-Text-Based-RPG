from encounter import *
from encounterGroup import *
from player import *
from name import *
import time


# A "game" organizes the necessary processes to play a game of Lugmere's Loss. It can process turns, and increment the
# total amount of turns.

#############
# CONSTANTS #
#############
STARTING_DOOM = 13
current_tamper = 0
TEXT_SPEED = 0.3

d = Dice()  # A dice to share with all the game mechanics.
n = Name()  # A name generate to share with all the writing.


# Pre: Given a string of text
# Post: Will split into lines and print each line out one at a time, waiting the specified time between lines.
def print_slow(str=""):
    for line in str.splitlines():
        print(line)
        time.sleep(TEXT_SPEED)

#    for letter in str:
#        sys.stdout.write(letter)
#        sys.stdout.flush()
#        time.sleep(TEXT_SPEED)


# Post: Waits for user to press ENTER.
def press_enter():
    input("[PRESS ENTER TO PROCEED]")


# Post: Presents an introduction
def opening_story():
    text_box("The Story So far...")
    print_slow('''
    Welcome to the Metropolis of Lugmere, a flying mechanical collection of floating isles, housing a population plagued 
    by rampant pollution and tense historical turmoil. Lugmere lives on its alien power source found at the center of 
    the capital, and trade economy ran by airships. Airships of all sizes and craft drift by the balconies of the 
    local populance as they fill the air with exhaust and advertisments. Every soul down to the rats know that falling 
    into the murky clouds below means certain death, but the tight alleyways and canals allow for lucky individuals to 
    grasp onto nearby buildings or other airships if they fell. However, it is not the distance that will end those poor 
    unlucky souls, but rather a horror so terrible that everyone lives in denial of its existence, except for 
    "The Mawful", a local cult who worships the being. They derive their will from this being, making the cult's 
    insignia of a headless body ever more appropriate.
    
    The cult has since been banished to the undercity of the metropolis, where they worship the being in secret. 
    Known as "The Maw", she sits underneath the entirety of Lugmere, lurking below the center of the capital, 
    waiting for her chance to swallow up poor souls who drift or fall too close. Her exact size is unknown, but 
    it is known that compared to her gargantuan size, Lugmere is but the tip of a pin. The origins of the beast remain 
    unknown as well, as she recently arrived 223 years ago. Researchers and professors of Lugmere's most prestigious
    "Orson Laboratories" theorize that she lost her way from The Outerworld, more specifically, the Kingdom of R'yleh.
    Her appearance triggered the occasional arrival of outerworldly beasts, who ambush travelers through mysterious 
    rifts.
    
    The Maw was sealed away 200 years ago with the help of a giant mechanical claw that grips so tight onto the beast 
    that at night, ear piercing wails of pain can be heard if you live close enough to the undercity district. Wires 
    stab into the creature so that with each cry, they light up to deliver power to the entire city. Strange liquids 
    ooze out of the wounds where the claw tears into The Maw, and is more cruel than even the most horrific of tortures.
    This is the heart of Lugmere, a literal beating of energy that paved the way for 200 years of unprecedented 
    developments in science and research.
    
    The world is ran on The Maw and a mysterious resource called "Flux". These delicate nugget sized ores are found 
    towards the base of all the isles, and glow with a tinge of light similar to electricity. Removing them will cause 
    the isle to slowly fall back to the surface, making Flux a limited resource. People have perished from
    simply dropping unrefined Flux, as a single unit is enough to explode an entire airship. Therefore, it is illegal to
    obtain vast quantities of the matter. It is also illegal to mine Flux from islands not dedicated to mining, because 
    it would doom anyone living on the landmass. Lugmere slowly lost its reliance on Flux in favor of The Maw, however 
    recent power surges and unidentifiable noises from The Maw forced the royal technicians to revisit the horror...
    
    ... The technicians reported that the beast is roaring and struggling, slowly weakening the grip of the
    floating prison. They estimate that even with continuous reinforcement and additional Flux that the clamp can't hold 
    out for much longer before The Maw escapes Lugmere's hold. A call has been made to all citizens of the metropolis 
    to prepare for one of two outcomes; for them to help find a solution, or band together to take down the beast.
    
    The announcement panicked the population, causing some to go insane or defect to the local cult. Either way, both
    victim's symptoms would warrant them a room in Lugmere's Insane Asylum. However, they are correct to fear fate, 
    because if The Maw escapes, Lugmere would revert to primitive times, using Flux again. The government knows that
    if this were to happen, Lugmere would be doomed because it would be only a matter of time before Flux becomes scarce,
    promoting stealing, violence, and Lugmere plummeting, returning to the surface once more.
    
    It is up to you to find a way to save Lugmere.
    
    ''')
    press_enter()
    print()
    help()


# Post: Prints out text that explains the premise of a regular turn.
def help():
    text_box("TAKING TURNS")
    print_slow('''
    THE OBJECTIVE OF THE GAME IS TO EARN THE HIGHEST SCORE. AT THE END OF THE GAME, EACH PLAYER'S SCORE IS CALCULATED 
    BASED ON THEIR TOTAL RESOURCES. THE GAME HAS 7 MAIN RESOURCES: 

    [Credits, Food, Fuel, Hull, Stress, Crew, Wisdom] 

    PLAYERS WHO RESOLVE THE MAW CONFLICT WILL GAIN A BONUS. 

    LUGMERE STARTS WITH A DOOM COUNTER OF 13. THE PLAYERS ENCOUNTER THE MAW WHEN THIS IS REDUCED TO 0.
    EACH TURN THE DOOM COUNTER TICKS DOWN BY 1.
        
    AT THE END OF EACH TURN, YOU MUST FEED YOUR PARTY INCLUDING YOURSELF, ONE FOOD EACH. IF YOUR CREW CANNOT BE FED,
    THEY WILL STARVE AND YOU WILL LOSE 5 SANITY PER DEATH.
    
    IF YOUR SANITY DROPS TO ZERO OR YOUR HULL DROPS TO ZERO, YOU BECOME DISABLED AND WILL SPEND TURNS TO RECOVER.
    IF YOU ARE DISABLED ON THE FINAL TURN, YOU WILL NOT ENCOUNTER THE MAW.   
        
     EACH TURN YOU CAN SELECT ONE OF SIX ACTIONS:   
        Mine - Only way to gain Flux (Fuel). May also gain crew and lose food.
        
        Dock - Only way to reduce Stress, replenish Hull, and gain Food. Consumes 10 credits per party member 
        (including yourself), per day.
        
        Work - Only way to gain Credits. Scales with amount of crew members (bigger workforce).
        
        Recruit - Consumes 50 credits to set up campaign. Gains crew members. Gaining crew this way gives wisdom.
        
        Tamper - Tampers with the doom counter. Can push it back 2 turns by sacrificing 5 crew members, or push it 
        forward 2 turns by spending 5 Flux. Will always cost 1 wisdom regardless. All players are saving their own 
        version of Lugmere, but everyone shares a Doom counter amongst each other.
        
        Explore - Consumes 1 Flux (fuel) and requires 1 Crew. Gives you a random encounter to possibly gain wisdom.
        Can gain or lose all types of resources, depending on your decisions.
    
    AT THE END OF THE GAME, EACH PLAYER'S SCORE IS CALCULATED. PLAYERS WHO RESOLVE THE MAW CONFLICT WILL GAIN A BONUS.
    ''')
    press_enter()


# Pre: Given a string,
# Post: Will print out the given string, but surrounded by "#".
def text_box(text):
    string = "# " + text + " #"
    print()
    print("#" * len(string))
    print(string)
    print("#" * len(string))


# Pre: Given an integer that represents the current turn,
# Post: Will carry out single player games for each of the players, and produce a scoreboard of final scores at the end.
def game_handler(doom):

    # Game setup
    player_count="-1"
    while player_count.isdigit() is False:
        player_count = input("How many people are playing Lugmere's Loss? ")
        if player_count.isdigit() is False:
            print("Please enter a number greater than 0.")
    players_normal = []
    for x in range(0, int(player_count)):
        players_normal.append(Player())
    i = 0
    while i < len(players_normal):
        players_normal[i].name = input("What is player " + str(i + 1) + "'s name? ") + " the " + n.generate_suffix()
        i += 1

    opening_story()

    # Regular game play
    players_insane = []
    while doom is not 0:
        text_box("The doom counter sits at " + str(doom) + "...")

        # Normal Condition
        for player in players_normal:
            if has_lost(player) is False:
                doom += process_turn(player)
                press_enter()
                player.update()
                press_enter()

            # Currently insane condition
            elif player in players_insane:
                print_slow(player.get_name() + " is currently insane. They try to snap out of it.")
                if d.roll(20) >= 15:
                    print_slow(player.get_name() + " has sucessfully come to their senses!")
                    player.resources[4] = 50
                    players_insane.remove(player)
                else:
                    print_slow(player.get_name() + " remains delusional...")
            else:

                # First time disabled
                if player.resources[4] == 0:
                    loss_by_sanity()
                    print_slow(player.get_name() + " has gone insane...")
                    players_insane.append(player)
                else:
                    print_slow(player.get_name() + " has to spend a day repairing their broken airship.")
                    player.add([0, 0, 0, 2, 0, 0, 0])
        doom -= 1

    # The Maw encounters only players fit to encounter
    for player in players_normal:
        if has_lost(player) is False:
            text_box(player.get_name() + " encounters The Maw.")
            player.score += encounter_maw(player)
        else:
            text_box(player.get_name() + " is disabled and does not encounter The Maw.")
    text_box("FINAL SCORES")
    i = 0
    while i < len(players_normal):
        print_slow(players_normal[i].get_name() + "'s SCORE IS: " + str(players_normal[i].score))
        i += 1


# Pre: Given a valid player object,
# Post: Processes one full turn for the player. After getting a course of action from the player, it performs it
# assuming the player has the resources to do so. If the action was not able to be performed (due to a lack of
# resources) it asks the player again for a different decision. It will return an integer based on the player's choices
# to be added to the doom counter.
def process_turn(player):
    text_box(player.get_name() + ", you have: ")
    print()
    player.get_count()
    print()
    press_enter()
    if player.resources[0] < 0:
        print_slow(player.get_name() + " is in debt!")
    print_slow()
    print("How do you spend your day?")
    choice = pick_choice(["Mine", "Dock [Costs 10 credits per crew member, including yourself]",
                          "Recruit [Costs 50 credits]", "Work", "Tamper [Costs 1 Wisdom, Minimum 5 Flux or 5 Crew]",
                          "Encounter [Minimum 1 Flux and 1 Crew]", "HELP"])
    doom_mod = 0
    if choice == 1:
        player.mine(d)
    elif choice == 2 and player.resources[0] >= 10*(player.resources[5]+1):
        player.dock(d)
    elif choice == 3 and player.resources[0] >= 50:
        player.recruit(d)
    elif choice == 4:
        player.work(d)
    elif choice == 5 and (player.resources[5] >= 5 or player.resources[2] >= 5) and player.resources[6] >= 1:
        doom_mod += tamper(player, 2)
    elif choice == 6 and player.resources[5] > 0 and player.resources[2] > 0:
        player.resources[2] -= 1
        encounter = exploration_encounters.get_random_encounter()
        player.add(encounter.get_outcome())
    elif choice == 7:
        help()
        process_turn(player)
    else:
        print_slow("You don't have the resources to do that. Please select another course of action.")
        process_turn(player)
    return doom_mod


# Pre: Given a list of strings that represent a choice the player can make,
# Post: Returns an integer representing the choice the player picked.
def pick_choice(choices):
    for x in choices:
        print(str(choices.index(x)+1) + ": " + x)
    while True:
        decision = None
        try:
            decision = int(input("ENTER 1-" + str(len(choices)) + ": "))
        except ValueError or decision not in range(1, len(choices)+1):
            print("That isn't an option.")
            continue
        if decision in range(1, len(choices)+1):
            return decision


# Pre: Given a player object and an integer that represents the degree of tampering/how much to impact the doom counter
# Post: Returns the degree as an integer to be added to the doom counter.
def tamper(player, degree):
    print_slow('''
    You decide to tamper with Lugmere's impending doom. What do you feel like doing?
    ''')
    choice = pick_choice(["Sacrifice 5 crew to The Maw [Pushes Doom Back]",
                          "Overload 5 Flux to the clamp on The Maw [Brings Doom Closer]"])
    if choice is 1 and player.resources[5] >= 5:
        print_slow("You sacrifice some crew members, and The Maw seems to calm down a little bit.")
        player.add([0, 0, 0, 0, 0, -5, -1])
        return degree
    elif player.resources[2] >= 5:
        print_slow("You overload the claw on The Maw, and she becomes agitated, struggling even more.")
        player.add([0, 0, -5, 0, 0, 0, -1])
        return -degree
    else:
        print_slow("You don't have the resources to do that.")
        tamper(player, degree)


# Pre: Given a player
# Post: Will check if the player has lost, which is when the player reaches 0 of two important resources.
def has_lost(player):
    return player.resources[3] == 0 or player.resources[4] == 0


##############
# ENCOUNTERS #
##############

# General Notes:
#
#   Encounter() constructor parameters are in the following order:
#   description, choice1, choice2, win message, win resources, lose message, lose resourced, mod, rating
#
#   The reward must be in a list in the standard resource order:
#   [Credits, Food, Fuel, Hull, Stress, Crew, Wisdom]


# EXPLORATION ENCOUNTERS:
exploration_encounters = encounterGroup()

exploration_encounters.add(Encounter(
    '''
    While traveling to your next destination, an unusual amount of fog engulfs your airship. A crew member,
    ''' + n.generate_name(True, False) + ''', spots that the color is a tinge of dark green, which you find unusual 
    compared to the smog that covers Lugmere. An eerie silence falls over you and your crew, as you all stare at each 
    other, unsure of where you're are, where you're going, and strangely, where you just came from. In fact, it is hard 
    to recall anything, even your own name, and you stare helplessly at the skies, not sure about anything. Shuffling 
    can be heard, and you soon see mite like creatures with oily bodies crawl up the side of your vessel and onto the 
    deck. You have free will, yet you don't feel inclined to warn your crew mates about the creatures crawling up their 
    legs. You can see them excreting a dark green gas, strikingly similar to the clouds that surround the airship. Tens 
    of these creatures slither across the deck, and one arrives at your feet, crawling up your leg. 
    It engulfs your head, and your thoughts are soon whisked away to another realm.
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
    [0, 0, 0, 0, -5*d.hidden_roll(4), 0, 4],
    '''
    You fail to meld with the creature, and you succumb to its gas. You wake to find your airship lodged into a random
    island, crew members are missing, and the early morning sun casting its light onto your face. Without a clue as to
    how long you were unconscious, you continue on your way, noting this encounter with the strange mite. 
    
    ''',
    [0, 0, 0, -4, -5*d.hidden_roll(6), -1*d.hidden_roll(4), 2],
    12,
    25
))

exploration_encounters.add(Encounter(
    '''
    One suspicion you've had with your dream about being swallowed by The Maw is that if you had not woken up early,
    perhaps you could have seen inside the horror herself, and understood more about the terror. Intrigued by this idea,
    you set out to explore dream and vision inducing drugs and ingredients. Your efforts have not gone unnoticed
    however, and eventually a strange figure approaches you in the night. ''' + n.generate_name() + ''' is dressed in a 
    robe that bears the insignia of \"The Mawful\", a cult that worships The Maw. They hand you a strange mushroom, and 
    tell you that ingesting it provokes strong dreams and visions. However, they explains that the plant has to be 
    dissolved in a concoction made from the blood and heart of a human, spelling death for whoever is chosen for such a 
    sacrifice. You figure you can make a similar concoction with a goat rather than a human. What do you do?
    ''',
    "Sacrifice one crew member",
    "Sacrifice a goat",
    '''
    Your mixture works, and you have a vivid dream about The Maw. You drift around the creature, and observe that it
    has a worm-like body with limbs that stretch all the way to the center of the world. You're able to count 18 
    distinct limbs whose length tangles with other limbs, producing a sea of snake like appendages. You realize Lugmere 
    is a mere tip of a needle in comparison to the size of the beast, and you are frightened as you awake, again in a
    pool of your own sweat.
    ''',
    [0, -1, 0, 0, -10, 0, 4],
    '''
    Your mixture fails. Perhaps the concoction wasn't made correctly, or maybe the mysterious plant was not to be
    trusted, but either way you feel horrible. Instead, you have a nightmare, and feel the wrath of The Maw as she 
    tears you apart. She harshly whispers to you in an unknown tongue, syllables piercing your brain. You awake on the
    floor, and your room is trashed. Your stomach is on fire and you have a terrible fever, but you push
    yourself to keep going, because the window to solve Lugmere's problem is quickly closing.

    ''',
    [0, -1, 0, 0, -20, 0, 1],
    3,
    13
))

exploration_encounters.add(Encounter(
    '''
    Desperate times call for desperate measures. After a rather troublesome trade with '''+n.generate_name()+''' from the
    undercity, you've finally gotten your hands on 2kg of skin from The Maw. It was freshly harvested not too long ago, 
    and several questionable aromas fill the air. This is your one chance to test the skin for any weaknesses, two of
    which you have in mind. One way to possible subdue The Maw would be with brute force, as an explosion made with
    enough Flux could possibly kill The Maw, so testing its weakness to Flux is an option. Another possibility is with
    an acidic poison, which could melt off important parts of The Maw, greatly disabling it. You are unsure if any of
    these approaches will work, and you can only test one because the skin sample will be rendered unusable after one
    test. Which do you choose?
    ''',
    "Attempt to blow up the skin with a Flux bomb.",
    "Attempt to melt the skin with a strong acidic poison.",
    '''
    What you're about to do is highly illegal, but it's for science. You travel to a deserted isle and strap a homemade
    Flux bomb to the piece of skin, arm it, and lob it off your airship to the ground below. It lands with a thud. Then
    silence. Suddenly, a giant explosion goes off and you see a huge crater. You move down to investigate. Walking over
    flames and burnt dirt, you find your specimen the skin sample was charred beyond recognition, guts spilling 
    out over the grass. The melted surface makes your blood curdle. It no doubt altered the skin. In fact, it seems to 
    pulse with some sort of renewed energy now, but looks like it will decay eventually. Perhaps The Maw amplifies Flux? 
    That would explain how it is able to pump the entirety of Lugmere with a similar source of energy, but surely that 
    Lugmere's government isn't that cruel..?
    ''',
    [0, 0, 0, 0, -4*d.hidden_roll(6), 0, 3],
    '''
    You get your hands on a strong acidic poison. The thick, gooey substance sits in a special vat, one made of a thin
    lining of Flux infused brass encased in a glass container. It resembles a museum exhibit, but one must go to such
    lengths to prevent the strong weapon from causing unecessary damage. You retreat to a deserted isle and throw the
    skin sample off the side of your airship. Shortly after, you open the container and carefully pour the poison 
    overboard and onto the skin. The vat empties, and on the isle sits a smoking column of burning plant material and
    dust. The substance burns a hold straight through the entire island, but fails to damage the skin sample, which was
    simple brushed aside by the substance. You can confidently conclude that The Maw is immune to poison.

    ''',
    [0, 0, 0, 0, -4 * d.hidden_roll(6), 0, 3],
    21,
    21
))

exploration_encounters.add(Encounter(
    '''
    While drifting through the clear night skies of Lugmere, you lay sleeping in your cabin. Your exhausted body quickly
    slips into a dream where you're standing on the viewing deck for the claw that clamps down on The Maw. You move
    closer to where the claw clamps on The Maw's body, and notice several hairs flowing around, as if The Maw herself
    was submerged in water. Several pieces of debris and spare copper parts float past you as you realize that
    everything lacks gravity. You float slowly towards The Maw and notice that her hairs are actually small suction
    cups held to her body by strings of flesh. The cups appear to be a perfect fit for a human head and you feel a 
    strong urge to meld with The Maw. She notices your presence and positions two strands of her hair towards you, each 
    with a different suction cup. One is lined with sharp teeth, and is pooling in blood, which oozes out between the
    teeth. The other looks like a flower, with a sweet nectar filling in the center. Which do you insert your head into?
    ''',
    "The sharp teeth pooling with blood.",
    "The flower flowing with nectar.",
    '''
    You insert your head into the suction cup, and it wraps around your neck. You're fully submerged in the liquid and
    can't breathe! You trust her and begin drinking what was in the cup rapidly, trying to get air. Your mind begins 
    slipping. You can feel The Maw inside of you, in your thoughts and heart. It invades you and fills you with the 
    deepest truths about the universe, about R'yleh and the otherworld, and what lies above and below Lugmere. You're 
    overwhelmed and quickly snap awake in your cabin on your airship. You can still taste the liquid in your mouth.
    ''',
    [0, -2, 0, 0, -d.hidden_roll(10), 0, 4],
    '''
    You insert your head into the suction cup, and it wraps around your neck. You're fully submerged in the liquid and
    can't breathe! You panic and try to get the suction cup off but it's too late- she has you. You deliver several
    blows to the suction cup, and your head can feel the impact of each of your punches. The Maw swiftly rips your
    neck in half, separating your head from your body. You feel an indescribable pain, which shocks you awake. You sit
    up in your cot, and quickly grasp your neck, relieved to find it still intact. Although it was a dream, it felt
    too close to reality. You have a suspicion that perhaps you should have trusted The Maw instead...

    ''',
    [0, -2, 0, 0, -5*d.hidden_roll(6), 0, 1],
    0,
    14
))

exploration_encounters.add(Encounter(
    '''
    While on your way to another destination, you pass by a mountainous floating island. This one is peculiar however, 
    because unlike other islands, this one lacks the typical white glow from Flux stones found at the base. Upon closer 
    investigation, you spot all the Flux stones removed and placed at the center of the island, sitting in a lone pile. 
    You find this strange because these stones are very valuable, yet they're just laying there. It is actually against 
    Lugmere law to possess that many stones, in order to limit one's total raw power output. Near the pile sits a hooded 
    figure, who appears to be badly wounded. The injured person notices your airship and yells out for help! On one hand 
    you can kill the person and take the Flux stones for yourself, as any witnesses would report you to the law. 
    On the other hand, you can help the figure, and hope they reward you with a share of Flux stones.
    ''',
    "Attempt to kill the injured person and steal the Flux stones.",
    "Attempt to help the injured person and hope for a reward.",
    '''
    As you land on the island and offload your crew, the hooded figure shakes off the red liquid you mistook for blood. 
    Your heart sinks at the sight of him revealing a horn from his robe. He blows on it loudly and suddenly from behind 
    the nearby mountains, several pirate airships appear and circle above! Realizing your mistake, you rush to grab as
    many Flux stones as you can, and leave on your airship. The pirates have trouble losing altitude to catch you before
    you're off on your way.
    ''',
    [0, 0, 40, 0, -5*d.hidden_roll(4), -2*d.hidden_roll(2), 0],
    '''
    As you land on the island and offload your crew, the hooded figure shakes off the red liquid you mistook for blood. 
    Your heart sinks at the sight of him revealing a horn from his robe. He blows on it loudly and suddenly from behind 
    the nearby mountains, several pirate airships appear and circle above! Realizing your mistake, you rush to grab as
    many Flux stones as you can, but the pirates descend on you. \"This isn't worth it.\" you tell yourself, as you drop
    the Flux stones and quickly escape.
    ''',
    [0, 0, 0, 0, -7*d.hidden_roll(4), -2*d.hidden_roll(4), 0],
    3,
    19
))

exploration_encounters.add(Encounter(
    '''
    You realize that with more credits you could accomplish so much more. Realizing the gravity of Lugmere's dilemma,
    you figure you can mount a pretty reasonable persuasive argument. You decide to approach '''+n.generate_name()+''', 
    the baron of a nearby fief on the outskirts of Lugmere for funding, as the central government only supports military 
    personnel. As you fly past downtrodden islands filled with poor villagers and farmland, you realize that this 
    particular baron does not treat his subjects kindly, and must be taxing them for more than the allotted amount. You 
    reason that being closer to the outskirts allows for more leniency with the law. Drifting closer to the baron's 
    reasonably elegant chateau prompts you to rethink your intentions. Should you still seek funding from the Baron, or 
    should you spread your wealth to the people?
    ''',
    "Seek help from the Baron.",
    "Give help to the poor.",
    '''
    You approach the Baron, and enter his hall. His slick skin and lofty demeanor is jarring in comparison to the poor
    local populance. You explain the news about The Maw's impending escape, and he is instantly shocked awake by the
    possibility of losing everything he owns. He sacrifices some of his greed to preserve his majority, and grants you
    credits. However, during the moment you reach out to accept it, you feel the disapproving gaze of your
    crew members. Your crew mates frown at your morality, as you're supposed to be saving Lugmere, not stealing from
    it, and some are disgusted enough to leave your cause!
    ''',
    [1000, 0, 0, 0, 0, -3*d.hidden_roll(3), 0],
    '''
    You have a change of heart and instead approach several of the downtrodden islands. On each island, you give 50
    credits, which for them should allow them to live comfortably until The Maw is dealt with. It also isn't a high
    enough amount to alert the baron, not that he would care about such a measly amount anyways. Your generosity is
    rewarded when several villagers are persuaded to join your cause! 
    ''',
    [-50*d.hidden_roll(4), 0, 0, 0, 0, 4*d.hidden_roll(4), 0],
    21,
    21
))

exploration_encounters.add(Encounter(
    '''
    As you drift through the skies, a giant swirling vortex suddenly opens up and a rift tears in the sky. The rift lets
    loose several small, dog sized fleshy bodies, armed with two legs and a sharp tail. Prior research helps you tell
    they're riftlings, which are outerworldy creatures from R'lyeh. You attempt to turn the airship around, but the 
    winds are not in your favor, and your engine fails to overcome the strength of the storm. Meanwhile, several
    riftlings fling themselves onto the deck of your airship and begin to cause panic. You're about to directly collide
    with the vortex, and you only have enough time to either steer away, or deal with the riftlings. What should you do? 
    ''',
    "Swerve the airship away from colliding with the vortex.",
    "Fight the riftlings on board.",
    '''
    From your flight cabin, you can hear horrible screams from the deck. You work to steer the airship away from the
    vortex, and manage to use the vortex to slingshot your craft out danger. As you leave, the vortex shrinks in size
    and the rift closes. A deafening silence falls over your ears as your crew stops screaming in pain, and you leave
    your flight cabin to investigate. You walk out to a horrible scene of carnage, with bits of riftlings dissolving
    into the air, and torn up crew members that line the railings. Several body parts are without owners, and you can
    hear the pleading of dying crew members as they crawl towards their captain, hoping you can save them. You put the
    dying crew members out of their misery, as their gashes are too large to heal. You turn to the side and see several 
    unscathed crew members paralyzed from shock and cowering in the corner. The threat is gone but the damage has been 
    dealt... 
    ''',
    [0, 0, 0, -1, -30, -2*d.hidden_roll(4)*d.hidden_roll(3), 6],
    '''
    You join your crew on deck to fight the riftlings. The background of the looming vortex frightens you, but your
    crew's morale instantly improves when they see you pull out your flintlock pistol and begin firing at the enemies.
    Your leadership and inspiration invokes vigor in your crew as you push back the riftlings. The creatures fling
    themselves about, using a pack mentality to attach and prey on individual crew members. Your teamwork 
    quickly cuts down their numbers. Unfortunately, the fight was the least of your concerns as your ship plunges into
    the vortex. You quickly usher your crew into the deepest cabins and you sit in fear and wait. You wait for what
    seems like an eternity. Suddenly, the storm yields, and a deafening silence falls over you and your crew. You 
    stumble outside only to find your airship wrecked immensely, and all that remains of the main deck are a few 
    floorboards and broken railings. 
    ''',
    [0, 0, 0, -2*d.hidden_roll(6), -30, -1*d.hidden_roll(4), 6],
    21,
    21
))

exploration_encounters.add(Encounter(
    '''
    Perhaps there are elder scholars and technicians on the outskirts of Lugmere who know more about the floating prison
    or about The Maw herself.  The district renown "Orson Laboratories" is the research facility for a collection of 
    professionals, some of which have grandfathers who worked on the original design and research for capturing and 
    utilizing The Maw. The hardest part isn't collecting information, as they're very open about their research, but 
    rather it is physically traveling to the lab to visit them. In order for them to run the most extreme experiments 
    regarding Flux power, they recluse themselves to the center of an active volcano on a large, mountainous floating 
    isle. You can't simply fly over to reach them because the heat from the lava produces too strong of an updraft to 
    land safely on the volcano. You'll have to land nearby and make a 11km trek on a well established path. 
    Alternatively you've heard of a cavern that shortens the trip to a mere 2km because it goes straight towards the 
    volcano. Both have been traveled previously by porters, however seasonal fluctuations in volcanic activity make it 
    hard to tell which is safer, especially when it comes to the cavern, because lava can quickly flood the cavern,
    trapping travelers inside. Additionally, recent activity by The Maw has stirred above ground activity in the 
    abominations and failed creations outcast by the Orson lab technicians, resulting in reports of ambushes by these 
    creatures. Which path do you choose? 
    ''',
    "11km path on the outside of the volcano.",
    "2km path on the inside of the volcano.",
    '''
    You safely traverse the volcano, failing to run into any major hindrances. An Orson lab technician, '''
    +n.generate_name()+''', shares with you that the claw holding The Maw in place is lacking Flux power 
    in the levers holding the clamp at its hinges. They figure that 30 more Flux would be enough to sustain the prison 
    for another 100 years. However, such an amount is illegal and hard to possess, and the idea is quickly dismissed by
    '''+n.generate_name()+''' a lab scholar who has another idea. They theorize that by sacrificing 30 people 
    to The Maw would calm her, claiming that it would satisfy her hunger. The Maw eats hundreds of people a year, 
    however they come in very small doses. A large amount at one time could calm her,giving Lugmere time to find a more 
    permanent solution. Armed with this information, you wait till the Orson lab professionals deem it safe to leave the 
    volcano, and you go on your way.
    ''',
    [0, -1*d.hidden_roll(2), 0, 0, -5*d.hidden_roll(2), 0, 6],
    '''
    Perhaps you made a bit too much noise. Or maybe you're just plain unlucky. But it was all going so well, until a
    sudden rumbling started to ring out. Suddenly, ahead of you lies a wave of lava rushing your group! You begin to
    quickly retreat, but the lava is quite quick. Several of your porters will definitely perish, and perhaps some
    crew members, but you'll have to take a headcount later. Orson's Laboratory will have to wait for another day...
    ''',
    [0, -2*d.hidden_roll(4), 0, 0, -10*d.hidden_roll(4), -1*d.hidden_roll(10)+1, 0],
    -4,
    13
))

exploration_encounters.add(Encounter(
    '''
    While traveling to your next destination, you can't help but feel like your airship is being followed. You're
    drifting a quite a low altitude, right around undercity level in fact, but there doesn't seem to be any cultists
    or pirates tailing behind you. Suddenly, from the murky clouds below, a giant snake like creature emerges and
    slithers towards your airship! Upon closer inspection, you notice there are teeth and claws all over the body, with
    dead bodies slathered onto the sharp weapons. Blood has coated most of the thing, and it unfortunately, it looks
    like there are a couple people still grasping onto life- must be freshly killed prey. You slowly realize this isn't 
    a creature, but rather one of the arms of The Maw herself. You know that this appendage is kilometers long, and 
    stretches to form seas of other \"snakes\" with her other arms. After some time of it tailing you, it comes to your 
    attention that the arm may be following the air drafts created by your airship. Contact would be horror and having 
    it grasp you would be instant death. Should you shut off your engines and wait for the arm to wander away, or should
    you accelerate faster to escape?
    ''',
    "Accelerate away and upwards.",
    "Shut off the engines.",
    '''
    The arm disappears into the distance and the coast is clear to continue on your way.
    ''',
    [0, 0, -1*d.hidden_roll(2), 0, -4*d.hidden_roll(6), 0, 2],
    '''
    The arm becomes larger and larger as it inches towards your airship. Everyone on board holds their breathe as the
    arm lurks closer. Even you cower, wondering what will happen next. Unfortunately, it swipes downwards with a 
    tremendous force, so strong that it shoots your airship off and out of the range of the arm. You peer out at your
    airship and find that the last quarter of it is missing. Some unlucky crew members are also gone. Even worse, some
    have been split in half or are missing body parts as they cling onto the remaining body of the airship. Blood and
    food splatters your deck as you realize the blow had damaged some of your crew and cargo. Crew members are in agony, 
    some are even swearing vengeance on The Maw. However, as these vengeful crew members slowly succumb to their 
    injuries, a depressing lull sets in... This was just a taste of The Maw's power.
    ''',
    [-100*d.hidden_roll(4), -2*d.hidden_roll(4), -1*d.hidden_roll(4), -2*d.hidden_roll(4), -6*d.hidden_roll(6),
     -1*d.hidden_roll(4), 6],
    -4,
    10
))

exploration_encounters.add(Encounter(
    '''
    While traveling over an island, you encounter a peculiar island. It is one of the few isles in Lugmere that has
    a secluded beach. You find it peculiar and decide to take a closer look. Upon landing and disembarking, you are
    greeted by a giant crowd of what appears to be sentient red crabs. They are about the size of an everyday chair, and 
    look like they weigh 40kg each. One of the crabs has a pale pinkish hue and is rather buff for a crab- clearly the 
    elder. It scurries up to you and you're shocked when you hear it speak! \"Hello humans. We are delighted by your 
    company. My name is ''' + n.generate_name(False, False) + ''' and we seek your aid. A nearby group of humans have 
    captured some of my brethren, planning to eat them, and this is unacceptable.\". They gesture with their giant claws 
    towards a nearby valley where you see several Mawful cultists gathered around a fire, slowly roasting a giant 
    screaming crab. You instantly sympathize because the cultists have roasted several humans alive as torture, so 
    seeing one of their own must be very painful for the crabs. There are two plans you and the crabs devise.
    ''',
    "Ride the crabs into battle in a giant stampede.",
    "Hide behind the crabs as they approach, then jump out to surprise the cultists.",
    '''
    The red crab elder charges and soon, several other crab soldiers follow in suit! They kick up dust and debris as
    hundreds of legs scurry down into the valley! The cultists react too late as they're taken by surprise when you
    are seen accompanying the army. They scramble and fail to find their weapons in time. You make quick work of the 
    cultists there, and help rescue the captured crabs. As a reward, the elder allows you to ransack the 
    cultist encampment.
    ''',
    [d.hidden_roll(3)*100, d.hidden_roll(10)*3, d.hidden_roll(4), 0, 0, 0, 0],
    '''
    The red crab elder charges and soon, several other crab soldiers follow in suit! They kick up dust and debris as
    hundreds of legs scurry down into the valley! The cultists jump up, weapons already in hand! They grab sticks of
    flame from the nearby roast, and scare away the crabs! They scuttle away in fear, afraid that they will be roasted
    as well. You and your crew continue to fight, and eventually deal with the cultists, but unfortunately with heavy
    losses. While you were distracted fighting the cultists, the crabs freed their brethren and made a quick
    escape. You're left with carnage all around you as dying cultists and crew members alike line the valley. You try
    to salvage what is left of the encampment.
    ''',
    [d.hidden_roll(100), d.hidden_roll(10), 1, 0, -6*d.hidden_roll(6),-3*d.hidden_roll(4), 2],
    3,
    13
))


# Pre: Given a player,
# Post: Will deliver the player through the content regarding the end of the game, and return an integer for the given
# player's final score at the end of the game.
def encounter_maw(player):
    choice1 = maw_phase1()
    choice2 = maw_phase2(player, choice1)
    if choice1 is 1:
        bonus = maw_phase3a(player, choice2)
    else:
        bonus = maw_phase3b(player, choice2)
    return bonus


# Post: Will return an integer that represents the player's choice in phase 1.
def maw_phase1():
    print_slow('''
    The clouds below Lugmere are swirling more violently as The Maw shakes and rattles the entire district. After
    traveling across the land for what seems like an eternity, you finally make your way back to the capital. As you
    approach the floating prison in the middle of the city, you realize you have a choice to make. How should you 
    approach saving Lugmere?
    ''')
    choice1 = pick_choice(["Attempt to kill The Maw. [CREW AND FLUX]",
                           "Attempt to seal The Maw. [CREW AND WISDOM]"])
    print_slow('''
    You drift closer to the gaping hole that forms beneath Lugmere. The Maw's stench of rotten flesh and dried blood
    fills your nose. You realize that you would rather take in Lugmere's musky smog than this scent. As you get
    closer, you can hear the hoarse breathing of The Maw. Her struggle and mere presence strikes fear into
    everyone on board.
    ''')
    return choice1


# Pre: Given a player and a decision made in phase 1,
# Post: Returns an integer that represents a choice the player made in phase 2.
def maw_phase2(player, choice1):
    player.add([0, 0, 0, 0, -d.hidden_roll(10), 0, 0])
    if choice1 == 1:
        print_slow('''
        A few ideas cross your mind. You can use the rest of your Flux and make a highly destructive bomb, capable of
        leveling even Lugmere if you have enough Flux, and drop it into The Maw's mouth. Or you can use the Flux to
        overload the claw clamping on The Maw and have it slice The Maw in two. Lastly, you can use your crew and 
        form a fleet to assault The Maw herself. How should you proceed?
        ''')
        choice2 = pick_choice(["Use a bomb. [FLUX]", "Overload the clamp. [FLUX AND OR CREW]",
                               "Organize an assault. [???]"])
    else:
        print_slow('''
        A few ideas cross your mind. You can use the collective conscience of your party's mind to assert dominance
        by melding with The Maw. Or you can make a precise sacrifice to The Maw, hoping to sate her hunger. Lastly, you 
        can release The Maw from the prison, hoping it will subdue herself, given the poor conditions of her captivity. 
        How should you proceed? 
        ''')
        choice2 = pick_choice(["Make a worthy sacrifice. [CREW]", "Group mind meld. [CREW AND WISDOM]",
                               "Release The Maw. [???]"])
    return choice2


# Pre: Given choice2, which was a decision made to kill the Maw
# Post: Returns an integer that represents the outcome of the chosen solution.
def maw_phase3a(player, choice):
    if choice is 1:
        print_slow('''
        You muster your crew to start assembling what might be the largest bomb Lugmere has ever seen. Due to
        strict laws on Flux, such a feat has not been attempted before until now. Everyone heaves in unison as
        they lug all the Flux on board into a pile. You carefully arrange and secure them in a bundle, and
        attach a timer. Soon, everyone is huddled in a circle around the creation, staring in awe. You look
        around, take a deep breathe, and slowly roll it off the side into the abyss. Everyone leans over the
        side of the airship, staring in silence as it disappears into the distance. You hear nothing, but see
        a giant flash of light. "Look away!" someone shouts, as everyone falls back.    
        ''')
        d.fake_roll(14)
        player.add([0, 0, -player.resources[2], 0, 0, 0, 0])
        if player.resources[2] >= 30:
            print_slow('''
            Shortly after, you hear the thunderous boom of the bomb, and your airship is thrust upwards by the 
            updraft! An ear piercing cry rings out, striking fear into everyone in Lugmere. Then silence. 
            An uncomfortable silence falls over the district; no more ambient growling or drafts from what used 
            to be The Maw. Such a peace tells you that the beast is definitely gone, but is it dead? That's a 
            question for another day. The updraft from the explosion carried you high above Lugmere, and you and 
            your crew watch the sun set, satisfied that Lugmere can live to see at least one more day. 
            ''')
            return 2500
        else:
            print_slow('''
            Shortly after, you hear a boom, which jolts your airship slightly. Everyone peers over the side to check
            the damage. You hear silence, then suddenly, The Maw lets out a thunderous roar... The bomb failed.   
            You tried your hardest but it's in vain. The Maw appears to have resisted your efforts just enough and 
            escapes the clamp holding her in place. Perhaps the bomb also damaged the claw? She rips out of the wires 
            and cords that connect here to Lugmere's power grid and she dives into the abyss of clouds below Lugmere, 
            quickly disappearing just as mysteriously as she appeared. 
            ''')
            return maw_effort_failure()
    elif choice is 2:
        print_slow('''
        You quickly move your airship to the viewing deck for the clamp. You organize your crew to transport the Flux
        into the main generator for the clamp. Everyone heaves in unison as they pass pieces of Flux to one another.
        ''')
        d.fake_roll(14)
        player.add([0, 0, -player.resources[2], 0, 0, 0, 0])
        if player.resources[2] >= 30 or (player.resources[2] >= 15 and player.resources[5] >= 15):
            print_slow('''
            You stuff the generator with an unprecedented amount of Flux, so dangerously packed that it could explode
            any minute and level the entirety of Lugmere. Not knowing if the generator can even process such a large
            amount, you rush up to the main control room, where you can get a good view of the prison clamping down
            on The Maw. The claws dig into The Maw's flesh, preventing it from escaping, but also causes immense
            suffering. You're about to make that pain so much more worse... You smash a glass box at the back of the 
            room and remove a key, which allows you to turn a dial past the marked limits on the dashboard. Shortly 
            after you turn it, you see the clamp vibrating, and The Maw instantly lets out an ear piercing cry! The
            Maw is trying to fight the pressure! You watch in horror as the brass clamp in one fluid motion, rips 
            through the fleshy body of The Maw, as if she had given up the struggle. It rips clean through her, and
            she is instantly silenced. Your jaw drops as you stare in awe at the stump that used to be The Maw. The 
            colossal severed body of The Maw falls into the abyss below Lugmere, disappearing from sight. No more
            will Lugmere's citizens have to wake up in fear that one day she may escape. Although Lugmere's main power
            source is gone, you're confident that this new found relief will give the population a reason to work
            together. 
            ''')
            return 2500
        else:
            print_slow('''
            You stuff the generator with as much Flux as you have. Not knowing if the generator can even process such an
            amount, you rush up to the main control room, where you can get a good view of the prison clamping down
            on The Maw. The claws dig into The Maw's flesh, preventing it from escaping, but also causes immense
            suffering. You're about to make that pain so much more worse... You smash a glass box at the back of the 
            room and remove a key, which allows you to turn a dial past the marked limits on the dashboard. Shortly 
            after you turn it, you see the clamp vibrating, and then it stops. You realize you've expelled all the
            power at one time, and failed to snap The Maw in two. Now, nothing is holding her back from slithering out.
            
            You tried your hardest but it's in vain. The Maw appears to have resisted your efforts just enough and 
            escapes the clamp holding her in place. She rips out of the wires and cords that connect here to Lugmere's 
            power grid and she dives into the abyss of clouds below Lugmere, quickly disappearing just as mysteriously 
            as she appeared. 
            ''')
            return maw_effort_failure()
    else:
        print_slow('''
        You trust your crew. You've been through the toughest and worst of times, some even sticking with you now.
        You're amazed that none of them have cowered in fear and fled, tail between their legs, rather deciding to help
        Lugmere and stop The Maw. "These men and women will make great soldiers" you tell yourself, and decide to lead
        them and mount a frontal assault on The Maw. You assemble your crew, along with local volunteers from Lugmere,
        into several airships armed with Flux cannons. They follow your airship as you spearhead the assault. You
        descend below the undercity of Lugmere, and enter the storm brewing below...
        ''')
        d.fake_roll(0, 5)
        print_slow('''
        A sea of snake like arms surround your army, forming walls that prevent your escape. You realize that you've
        underestimated the sheer size and power of The Maw, as she closes her grip around you. You command your army to
        begin firing the cannons, and they let loose a volley of volatile Flux projectiles, which seem to only be
        absorbed into the tough hide of The Maw. It seems with each volley, The Maw grows stronger. Perhaps The Maw
        is immune to Flux? She draws closer and closer, as her arms proceed to swat your army out of the air as if they
        were flies. Soon enough, it is just you and her, and she stares are you with 1,000 eyes. They all blink at
        different times, producing a shimmering sequence of enraged stares. She grins a giant smile, revealing her
        blood covered teeth, covered with severed human bodies. The Maw opens her mouth and swallows you into darkness.
        With no one left to stop her, escaping from her prison is only a matter of time...
        ''')
        return maw_effort_failure()


# Pre: Given choice2, which was a decision made to seal the Maw
# Post: Returns an integer that represents a bonus to be added to the player's score for the chosen solution. Some
# solutions lead to an additional sanity event as a last ditch effort to defeat the maw.
def maw_phase3b(player, choice):
    if choice is 1:
        print_slow('''
        Desperate times call for desperate measures. There is no easy way to say it, so you decide to be blunt.
        You round up all your naive crew members on the upper main deck, and tell them that they are going to be 
        sacrificed to The Maw. The majority of them are surprisingly willing to sacrifice themselves for Lugmere, 
        however there are always those who prefer to save themselves rather than die for their people. The protesting 
        is getting worse, and soon they begin to persuade others. You've already committed to this decision, and there 
        isn't enough time to choose a different course of action. You decide to lock your entire crew on the upper main
        deck while you retreat to the pilot's cabin. While bickering among themselves, you move the airship even closer
        to The Maw. Your hands shake at what you're about to do next. You whisper "Please forgive me" as you rotate
        your airship on it's side, causing your crew to fall off, straight into The Maw's gaping mouth. You can hear
        panic, enraged screaming mixed in with pleading and praying as some crew members managed to grip to the ship.
        You can't let them live, not after what you just did. You continue to tilt the airship...
        ''')
        d.fake_roll(10)
        if player.resources[5] >= 30:
            print_slow('''
            As you watch the last crew member plummet to their doom, you fly to a safe distance and wait in
            silence. You ponder your decision, and know that you will live in grief forever for what you just did. 
            Suddenly however, The Maw stops struggling. It simply stops resisting the prison, and sits content, almost 
            groaning with satisfaction. It is a strangely peaceful sight, and you realize your sacrifice has sated The
            Maw. No more will Lugmere's citizens have to wake up in fear that one day she may escape, because right now,
            there seems to be no effort. You've bought more time for Lugmere to find a more permanent solution, but
            maybe making large scale sacrifices is the future? You've changed Lugmere in more ways than you can imagine.
            ''')
            return 2500
        else:
            print_slow('''
            As you watch the last crew member plummet to their doom, you fly to a safe distance and wait in
            silence. You ponder your decision, and know that you will live in grief forever for what you just did. You
            realize you've been pondering for a while, and nothing has changed. The Maw still lets out irritating
            cries while she thrashes about in the prison. 
            ''')
            return maw_sanity_failure()
    elif choice is 2:
        print_slow('''
        You and your crew drift closer to the viewing deck for The Maw's prison. You gaze across the clouds to see a
        giant claw digging into the body of the beast, clenching it in place, albeit for not much longer. You can hear
        the creaking of the metal as it begins to weaken, so time is of the essence. You land and walk across the deck
        of the viewing platform until you and your crew are face first with the surface of The Maw. You take a look.''')
        d.fake_roll(14)
        print_slow('''
        A closer inspection of the hairs that line the beast reveal that they are actually small suction cups held to 
        her body by strings of flesh. They appear to be human sized, and look like all sorts of types, from sharp, razor
        teeth linings, to beautiful flower like flaps that ooze nectar. A nearby Maw prison station manager explains
        that several workers have died trying to explore the strange opportunity, and that the ones who have lived went
        insane, living out the rest of their days in Lugmere's Insane Asylum. You tell your crew to each take a cup
        and engulf their head. Some choose appendages that appear like creatures, others choose the ones shaped like
        flowers. Regardless, they are all quite grotesque and ooze different strangely colored liquids. You trust the
        mental fortitude of your crew, as you have been together through a lot. Everyone fearfully dons the helmets and 
        are whisked away in mind and spirit into The Maw.
        ''')
        print_slow('''
        You find yourself worrying. You are lost in your thoughts, and can picture yourself, but from a perspective
        outside of your body. You see yourself with your crew standing at the skin of the creature. Flashes of light
        cloud your vision, and you feel like you're being squished.
        ''')
        d.fake_roll(17)
        print_slow('''
        You sucessfully resist the pressure, pushing back with a force much greater. You can hear the thoughts of
        all your crew members, as they cheer and egg each other on. You push harder, not physically, but just
        enough to resist the pull of The Maw. 
        ''')
        if player.resources[5] >= 20 and player.resources[6] >= 10:
            d.fake_roll(12)
            print_slow('''
            You can feel The Maw weakening. It seems that her endurance is waning, and you and your crew take this as
            a chance to push her out. You feel your souls climb higher and higher into her mind as you soar past
            vivid colors and sights of gore. Entering her mind is both scary but encouraging, and you're one step closer
            to sealing her for good. Suddenly, you find yourself at the heart of her mind, and her struggle ceases.
            Your mind slowly melds with her's and your thoughts are jumbled with her intentions. You feel the pain of
            the prison clamping down on you, and Lugmere's constant jabbing for power. Suddenly, your mind is clouded
            by the thoughts of your other crew members, as everyone floods into the same consciousness. You find it 
            impossible to control The Maw's actions, and everyone's will is against a collected composure. As a result,
            she stands still. So still that you notice what her eyes see, or rather, your eyes now. You peer out from
            the center of Lugmere and see that the district has completely changed. Instead of what once was a dirty 
            city is now a pristine, glowing, lofty collection of polished buildings and unknown technology. You notice
            that at the center of the main square of Lugmere is a display.. You peer closer and find it dedicated to
            you and your crew! You swear you were only gone for a mere hour in the mental battle, but you realize that
            the time must have passed one hundred fold. Your happiness for the new state of Lugmere is quickly
            overshadowed by the depression that sets in because of your current state, You wonder how you can escape
            the seemingly eternal torment you feel as the claw prison digs into your body.
            ''')
            return 2500
        else:
            d.fake_roll(0, 4)
            print_slow('''
            Suddenly, her power increases. Out of what seems like nowhere, she thrusts you and your crew's mental states
            into hell. Violence and horror are all that fill your minds, and you quickly become scared. So scared in 
            fact that you can't bear her terrible mindscape any longer, and you wish to escape. You feel your 
            perspective shift inwards as you travel back towards your body. You try to collect your conscience and
            identity as you quickly flush yourself back out into reality. You find yourself, helmet off, back in 
            Lugmere, and you collapse onto the ground.
            ''')
            return maw_sanity_failure()
    else:
        print_slow('''
        You see that The Maw is in a lot of pain. You wonder, just maybe, if by releasing The Maw from her pain that
        she would be subdued in that manner. You drift your airship down to the station that manages The Maw's clamp.
        As you approach the main control room, a technician stops you. His gruff demeanor and stature tells you he is
        a stickler for the rules... Telling him you're releasing The Maw undermines the entire purpose of the facility
        so you'll have to persuade him to pass.
        ''')
        d.fake_roll(17)
        print_slow('''
        You tell him that have a plan to stop The Maw and that you need access to the main dashboard. He barely seems
        satisfied, but lets you through. You and some crew members walk into the room, and realize that it is flooded
        with technicians. You'll need to remove them all if you're to release The Maw, since they are most likely going
        to hinder and arrest you in the process.
        ''')
        d.fake_roll(16)
        print_slow('''
        You and your crew carefully arrange yourself in the room around the busy technicians. Simultaneously your crew 
        dispatches them all at once, while you quickly seal the door! You can hear pounding on the outside, and alarms
        blaring. The gruff technician from earlier is screaming and cursing at you from the other side of the lock!
        You casually make your way to the emergency release switches, smash the glass boxes protecting them, and have 
        you and your crew simultaneously turn 5 knobs and push it in. Suddenly everything stops, the alarms are silent,
        the station dims its lights, even the gruff technician stares at you in horror. The only source of light is the
        power surging out of The Maw, as the claw holding her in place releases smoke and steam. It opens, and she sits
        there, tension filling all of Lugmere. Suddenly, she lets out a terrible roar and makes her move. She rips out 
        of the wires and cords that connect here to Lugmere's power grid and she dives into the abyss of clouds below 
        Lugmere, quickly disappearing just as mysteriously as she appeared. 
        ''')
        return maw_effort_failure()


def maw_effort_failure():
    print_slow('''
    From this day on, Lugmere will remain in a state of decay. When The Maw left, she took Lugmere's electricity with 
    her. Many power generators will revert back to using Flux, which is slowly but surely becoming more and more scarce. 
    Because this non renewable resources holds up the islands, it won't be long before war breaks out in Lugmere, as 
    islands will begin to turn on each other for their Flux. You realize this is the end of an era, and that Lugmere 
    will fall back to more primitive ways.
    
    The fear that The Maw might one day return haunts every citizen of Lugmere, which will eventually cause the
    government to break down. Perhaps if the threat was really gone, Lugmere might be able to find a new beginning in
    this state of decay, but unfortunately, Lugmere will forever be in the dark... That is, until The Maw returns for
    vengeance.
    ''')
    return 100


def maw_sanity_failure():
    print_slow('''
    You grieve for Lugmere. The sheer power of The Maw has gotten into your mind and is messing with your thoughts. You
    collapse into a state of isolation, and feel the need to do nothing. You no longer care about this world, or the
    next, and no longer worry about Lugmere. But this isn't a state of peace, but rather a state of longing. You long
    for Her, and wish to connect with The Maw. You can't help but spend the rest of your days, cradled up and whispering
    incoherent phrases to yourself. You're quickly sent to Lugmere's Insane Asylum where you spend the rest of your days
    staring at a blank wall. You can't wait for Lugmere's inevitable demise.
    ''')
    return 100


def loss_by_sanity():
    print_slow('''
    You can't take it anymore. Your head pulses with all the horrors of R'yleh, and you feel like there are 
    things you are not supposed to know. You wake up in the morning in a daze. Doctors don't know what's wrong with you. 
    People say you repeat phrases like "it's hopeless" or "she's won", little snippets that have caused your closest 
    friends to check you into Lugmere's asylum for the insane. You don't care, why would you anyways? The only thing 
    that matters is her. She fills your thoughts all day, and it feels like she's talking to you. 
    "Come child, I need you" she says. The line between your thoughts and reality blurs. No one visits you because you 
    feel like no one understands you. Your only visitors are strange hooded figures. They bear the insignia of 
    The Mawful on their chest; a headless person. One of them reaches a hand out to you, and repeats 
    "Come child, I need you", and you take their hand...
    ''')


# Starts a game of Lugmere's Loss.
game_handler(STARTING_DOOM)





