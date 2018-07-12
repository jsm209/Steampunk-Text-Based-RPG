from encounter import *
from encounterGroup import *
from player import *

# A "game" organizes the necessary processes to play a game of Lugmere's Loss. It can process turns, and increment the
# total amount of turns.

#############
# CONSTANTS #
#############
MAX_TURNS = 13

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
def player_turn(player, turn, max_turns):
    if turn <= max_turns and has_lost(player) is False:
        print()
        print("-" * 50)
        print("It is the start of day " + str(turn) + " of " + str(max_turns) + ".")
        process_turn(player)
        player.update()
    else:
        print("Maw Encounter")
        # After MAX_TURNS, encounter The Maw.


# Pre: Given a list of players,
# Post: Will carry out single player games for each of the players.
def game_handler(players, turn, max_turns):
    while turn <= max_turns:
        print("-" * 50)
        print("It is the start of day " + str(turn) + " of " + str(max_turns) + ".")
        print("-" * 50)
        for player in players:
            if has_lost(player) is False:
                process_turn(player)
                player.update()
        turn += 1
    print("Maw Encounter")
    # After MAX_TURNS, encounter The Maw.


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
            choice = int(input("[ENTER ANY NUMBER 1-5:] "))
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
    print()
    print("-" * 50)
    print(player.get_name() + ", you have: ")
    print("-" * 50)
    print()
    player.get_count()
    print()
    print("How do you spend your day?")
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
    elif choice == 5 and player.resources[5] > 0 and player.resources[2] > 0:
        player.resources[2] -= 1
        player.resources[5] -= 1
        encounter = exploration_encounters.get_random_encounter()
        player.add(encounter.get_outcome())
    else:
        print("You don't have the resources to do that. Please select another course of action.")
        print("You figure exploration and research both need at least one crew member and one Flux stone.")
        process_turn(player)


# Pre: Given a player
# Post: Will check if the player has lost, which is when the player reaches 0 of two important resources.
def has_lost(player):
    return player.resources[3] == 0 or player.resources[4] == 0


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

research_encounters.add(Encounter(
    '''
    Desperate times call for desperate measures. After a rather troublesome trade with a shady character from the
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
    flames and burnt dirt, you come to a shocking sight; the skin sample was charred, but beyond that it was completely
    unharmed. It no doubt altered the skin, but not in any damaging way. In fact, it seems to pulse with some sort of
    energy now, but looks like it will decay eventually. Perhaps The Maw is immune to Flux? That would explain how it 
    is able to pump the entirety of Lugmere with a similar source of energy, but surely that energy and Flux can't be 
    the same thing..?
    ''',
    [0, 0, 0, 0, -2*d.hidden_roll(6), 0, 2],
    '''
    You get your hands on a strong acidic poison. The thick, gooey substance sits in a special vat, one made of a thin
    lining of Flux infused brass encased in a glass container. It resembles a museum exhibit, but one must go to such
    lengths to prevent the strong weapon from causing unecessary damage. You retreat to a deserted isle and throw the
    skin sample off the side of your airship. Shortly after, you open the container and carefully pour the poison 
    overboard and onto the skin. The vat empties, and on the isle sits a smoking column of burning plant material and
    dust. The substance burns a hold straight through the entire island, but fails to damage the skin sample, which was
    simple brushed aside by the substance. You can confidently conclude that The Maw is immune to poison.

    ''',
    [0, 0, 0, 0, -2 * d.hidden_roll(6), 0, 2],
    21,
    21
))

research_encounters.add(Encounter(
    '''
    While drifting through the clear night skies of Lugmere, you lay sleeping in your cabin. Your exhausted body quickly
    slips into a dream where you're standing on the viewing deck for the claw that clamps down on The Maw. You move
    closer to where the claw clamps on The Maw's body, and notice several hairs flowing around, as if The Maw herself
    was submerged in water. Several pieces of debris and spare copper parts float past you as you realize that
    everything lacks gravity. You float slowly towards The Maw and notice that her hairs are actually small suction
    cups held to her body by strings of flesh. The cups appear to be a perfect fit for a human head and you feel a 
    strong urge to meld with The Maw. She notices your presence and positions two strands of her hair towards you, each 
    with a different suction cup. One is lined with sharp teeth, and is pooling in blood, which oozes out between the
    teeth. The other looks like a flower, with a nectar filling in the center. Which do you insert your head into?
    ''',
    "Trust the sharp teeth and enter the blood.",
    "Trust the flower and enter the nectar.",
    '''
    You insert your head into the suction cup, and it wraps around your neck. You're fully submerged in the liquid and
    can't breathe! You trust her and begin drinking what was in the cup rapidly, trying to get air. Your mind begins 
    slipping. You can feel The Maw inside of you, in your thoughts and heart. It invades you and fills you with the 
    deepest truths about the universe, about R'yleh and the otherworld, and what lies above and below Lugmere. You're 
    overwhelmed and quickly snap awake in your cabin on your airship. You can still taste the liquid in your mouth.
    ''',
    [0, 0, 0, 0, -d.hidden_roll(6), 0, 3],
    '''
    You insert your head into the suction cup, and it wraps around your neck. You're fully submerged in the liquid and
    can't breathe! You panic and try to get the suction cup off but it's too late- she has you. You deliver several
    blows to the suction cup, and your head can feel the impact of each of your punches. The Maw swiftly rips your
    neck in half, separating your head from your body. You feel an indescribable pain, which shocks you awake. You sit
    up in your cot, and quickly grasp your neck, relieved to find it still intact. Although it was a dream, it felt
    too close to reality. You have a suspicion that perhaps you should have trusted The Maw instead...

    ''',
    [0, 0, 0, 0, -2*d.hidden_roll(6), 0, 1],
    0,
    14
))

# EXPLORATION ENCOUNTERS:
exploration_encounters = encounterGroup()
exploration_encounters.add(Encounter(
    '''
    While on your way to another destination, you pass by a mountainous floating island. This one is peculiar however, 
    because unlike other islands, this one lacks the typical white glow from Flux stones found at the base. Upon closer 
    investigation, you spot all the Flux stones removed and placed at the center of the island, sitting in a lone pile. 
    You find this strange because these stones are very valuable, yet they're just laying there. It is actually against 
    Lugmere law to possess that many stones, in order to limit one's total raw power output. Near the pile sits a hooded 
    figure, who appears to be badly wounded. The injured person notices your airship and yells out for help! On one hand 
    you can kill them and take the Flux stones for yourself, as any witnesses would report you to the law. 
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
    [0, 0, 30, 0, -5, -1, 0],
    '''
    As you land on the island and offload your crew, the hooded figure shakes off the red liquid you mistook for blood. 
    Your heart sinks at the sight of him revealing a horn from his robe. He blows on it loudly and suddenly from behind 
    the nearby mountains, several pirate airships appear and circle above! Realizing your mistake, you rush to grab as
    many Flux stones as you can, but the pirates descend on you. \"This isn't worth it.\" you tell yourself, as you drop
    the Flux stones and quickly escape.
    ''',
    [0, 0, d.hidden_roll(3), 0, -10, -1*d.hidden_roll(4), 0],
    3,
    19
))

exploration_encounters.add(Encounter(
    '''
    You realize that with more credits you could accomplish so much more. Realizing the gravity of Lugmere's dilemma,
    you figure you can mount a pretty reasonable persuasive argument. You decide to approach the baron of a nearby
    fief on the outskirts of Lugmere for funding, as the central government only supports military personnel. As fly
    past downtrodden islands filled with poor villagers and farmland, you realize that this particular baron does not
    treat his subjects kindly, and must be taxing them for more than the allotted amount. You reason that being closer
    to the outskirts allows for more leniency with the law. Drifting closer to the baron's reasonably elegant chateau 
    prompts you to rethink your intentions. Should you still seek funding from the Baron, or should you spread your 
    wealth to the people?
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
    [1000, 0, 0, 0, 0, -2*d.hidden_roll(3)+d.hidden_roll(3), 0],
    '''
    You have a change of heart and instead approach several of the downtrodden islands. On each island, you give 50
    credits, which for them should allow them to live comfortably until The Maw is dealt with. It also isn't a high
    enough amount to alert the baron, not that he would care about such a measly amount anyways. Your generosity is
    rewarded when several villagers are persuaded to join your cause! 
    ''',
    [-50*d.hidden_roll(4), 0, 0, 0, 0, 2*d.hidden_roll(3), 0],
    21,
    21
))

exploration_encounters.add(Encounter(
    '''
    As you drift through the skies, a giant swirling vortex suddenly opens up and a rift tears in the sky. The rift lets
    loose several small, dog sized fleshy bodies, armed with two legs and a sharp tail. Prior research helps you tell
    they're riftlings, which are otherworldy creatures from R'lyeh. You attempt to turn the airship around, but the 
    winds are not in your favor, and your engine fails to overcome the strength of the storm. Meanwhile, several
    riftlings fling themselves onto the deck of your airship and begin to cause panic. What should you do? 
    ''',
    "Steer the airship away from colliding with the vortex.",
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
    [0, 0, 0, -1, -20, -2*d.hidden_roll(3)*d.hidden_roll(3), 2],
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
    [0, 0, 0, -2*d.hidden_roll(3), -20, -1, 2],
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
    hard to tell which is safer, especially when it comes to the cavern. Additionally, recent activity by The Maw has 
    stirred above ground activity in the abominations and failed creations outcast by the Orson lab technicians, 
    resulting in reports of ambushes by these creatures. Which path do you choose? 
    ''',
    "11km path on the outside of the volcano.",
    "2km path on the inside of the volcano.",
    '''
    You safely traverse the volcano, failing to run into any major hindrances. The Orson lab technicians share with you
    that the claw holding The Maw in place is lacking Flux power in the levers holding the clamp at its hinges. They 
    figure that 30 more Flux would be enough to sustain the prison for another 200 years. However, such an amount is 
    illegal and hard to possess, and the idea is quickly dismissed by the lab scholars who have another idea. They 
    theorize that by sacrificing 30 people to The Maw would calm her, claiming that it would satisfy the outerworld. 
    One core reason they believe this will work, is because there have been eyewitness accounts of a portal located 
    inside The Maw's mouth, which is similar in appearance to those that lead to the outerworld. Armed with this 
    information, you wait till the Orson lab professionals deem it safe to leave the volcano, and you go on your way.
    ''',
    [0, -1*d.hidden_roll(2), 0, 0, -5*d.hidden_roll(2), 0, 2],
    '''
    Perhaps you made a bit too much noise. Or maybe you're just plain unlucky. But it was all going so well, until a
    sudden rumbling started to ring out. Suddenly, ahead of you lies a wave of lava rushing your group! You begin to
    quickly retreat, but the lava is quite quick. Several of your porters will definitely perish, and perhaps some
    crew members, but you'll have to take a headcount later. Orson's Laboratory will have to wait for another day...
    ''',
    [0, -2*d.hidden_roll(2), 0, 0, -10*d.hidden_roll(2), -1*d.hidden_roll(4)+1, 0],
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
    [0, 0, -1*d.hidden_roll(2), 0, -3*d.hidden_roll(5), 0, 0],
    '''
    The arm becomes larger and larger as it inches towards your airship. Everyone on board holds their breathe as the
    arm lurks closer. Even you cower, wondering what will happen next. Unfortunately, it swipes downwards with a 
    tremendous force, so strong that it shoots your airship off and out of the range of the arm. You peer out at your
    airship and find that the last quarter of it is missing. Some unlucky crew members are also gone. Even worse, some
    have been split in half or are missing body parts as they cling onto the remaining body of the airship. Blood and
    food splatters your deck as you realize the blow had damaged some of your cargo. Crew members are in agony, some
    are even swearing vengeance on The Maw. However, as these vengeful crew members slowly succumb to their injuries,
    a depressing lull sets in... This was just a taste of The Maw's power.
    ''',
    [-100*d.hidden_roll(4), -1*d.hidden_roll(4), -1*d.hidden_roll(4), -1*d.hidden_roll(4), -5*d.hidden_roll(5), -1*d.hidden_roll(4), 3],
    -4,
    10
))


def encounter_maw(player):
    print('''
        This is it
    ''')


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


# Starts a game of Lugmere's Loss.
p1 = Player()
p2 = Player()
players = [p1, p2]
game_handler(players, 1, MAX_TURNS)





