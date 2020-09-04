from room import Room
from player import Player
import item
import creature
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'platform': Room("platform", "Distant Platform", """Desolate, fire-scorched plateau. The rocky surface is littered with the bones of past adventurerers."""),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied of treasure by earlier adventurers. The only exit is to the south."""),

    'top': Room("top", "Top of Mountain", """The icy, rocky crag juts up above the clouds. You can no longer see the cave or the desert! You shiver with the cold in the icy wind that whistles around you."""),

    'secret': Room("secret", "Secret Cavern" ,"""DESCRIPTION"""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['platform']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create items

item = {
    'rock': item.Item("rock", "Plain desert rock. Dark sandy color."),

    'skull': item.Item("skull", "Old skull, aged and worn. Probably a piece of a past adventurer. Possibly gnawed on? Huh, I wonder what did that?"),

    'femur': item.Item("femur", "Old and riddled with teethmarks. Creepy!"),

    'coins': item.Item("coins", "Small pile of gold coins."),

    'chest': item.Item("chest", "Little wooden chest. Rattles when shaken. Locked."), # normal item, but the key opens a portal in it for the dragon egg nest with replinishing food and necessary items for baby-dragon-rearing.

    'club': item.Weapon("club", "This is a wooden club, worn smooth with age. Used to kock into creatures.", "blunt"),

    'sword': item.Weapon("sword", "This is a dull sword, rusty with lack of care and use. Used to slice through creatures.", "dull"),

    'pick': item.Weapon("pick", "This is a sharp ice pick, long and thin and sturdy. Used to stab into ice...and fleshy creatures.", "sharp"),

    'key': item.Magical_Item("key", "Little brass key. Looks like it fits a small chest? Sparkling lightly.", "unknown"), # fits chest

    'sculpture': item.Magical_Item("sculpture", "Small wooden sculpture of voloptuous naked woman. A fertility goddess. You can feel the power eminating from her!", "transport"), # takes you to secret cavern

    'stick': item.Magical_Item("stick", "Thin, brittle looking stick. Much stronger looking than it appears. Cursed.", "transport"), # cannot enter treasure room with this, it will transport you back to the Outside if holding it

    'treasure': item.Treasure("treasure", "DESCRIPTION")
}

# Add items to rooms

def reset_room_items():
    room['outside'].items = [item['rock'], item['club']]
    room['foyer'].items = [item['rock'], item['coins'], item['pick']]
    room['overlook'].items = [item['skull'], item['femur'], item['coins'], item['chest'], item['stick']]
    room['platform'].items = [item['rock'], item['skull'], item['femur']]
    room['narrow'].items = [item['rock'], item['femur'], item['coins'], item['sword']]
    room['treasure'].items = [item['rock'], item['skull'], item['femur'], item['sculpture'], item['coins'], item['key']]
    room['top'].items = [item['rock'], item['skull'], item['femur']]
    room['secret'].items = [item['coins'], item['treasure']]

# Create Creatures

# - statements
mouse_options = ["Welcome to the cave! I hope your journey is going well!", "The platform may be interesting from afar, but its scary in person!", "The treasure room feels pretty powerful...", "I thought I heard a noise past the end of the cave once...", "One of the scary dragons is actually pretty awesome, if you can avoid being eaten!"]

bat_options = ["There's a couple items that are absolutely needed in here.", "Listen to the mouse. He gives some good advice.", "Don't make the ghost angry. You won't like him when he's angry.", "Who is the goddess of fertility? I can't quite remember.", "Curses can be removed if you try hard enough."]

lizard_options = ["Do you have any bugs. I like bugs.", "Are *you* edible. We're awfully hungry. Just kidding. Do you have any bugs?", "I found a key. It's shiny. It wasn't edible though. 🥺", "Where do you live? I live under a rock. Do you want to come live under my rock with me?", "I tried to eat a stick once and my mouth went all tingly. I didn't like it.", "There's a hidden room you know.", "One of the BIG lizards has a secret!!!", "Many years ago we had visitors here. They were yummy. I'm sure you're safe though. 😃", "Did you know BIG lizards are immortal?", "Can you take me with you if you survi-- I mean win?", "🎶 I believe in magic 🎶", "*** Weird Lizard Noises ***", "The ghost is very grumpy.", "Please don't eat me! I swear I don't taste like chicken.", "Look for the BIG green lizard."]

ghost_options = ["What the 🤬 do you want?", "Don't bother me!", "I'd leave the dragons alone, if I were you.", "You should quit now, you won't win...", "Do you know any riddles?"]

fire_options = ["How dare you invade my home. There is nothing for you here but death!", "My fire will bring eternal pain!", "There is no escape, only the fire from my breath!"]

ice_options = ["You should have never enraged the ghost.", "Because of your foolishness, the Cave will be sealed for a Very Long Time.", "May your descendants have better luck."]

life_options = ["Life is beauty.", "We are dying, but there is hope, with you, brave adventurer.", "I hope you live up to the tests of this Cave."]

egg_options = ["*High pitched whine*", "*Muffled gurgle*", "*Soft rustle of scales on eggshell*"]

# - creatures
creature = {
    'mouse': creature.Friendly("mouse", "Small grey animal with fur. Long naked tail.", mouse_options, "mammal"),
    'bat': creature.Friendly("bat", "Large scary looking bat. Looks ferocious, actually a vegetarian.", bat_options, "mammal"),
    'lizard': creature.Friendly("lizard", "Tiny green lizard. Zips around quickly along any surface...even ceilings. Easily distracted.", lizard_options, "reptile"),
    'ghost': creature.Grumpy("ghost", "Shimmery and translucent. Mumbles grumpily to itself as it floats around the room. Seems agitated.", ghost_options, "dead"),
    'fire_dragon': creature.Dragon("fire_dragon", "Giant red dragon with powerful black wings.", fire_options, "red", "fire"),
    'ice_dragon': creature.Dragon("ice_dragon", "Huge blue dragon with webbed teal wings.", ice_options, "blue", "ice"),
    'life_dragon': creature.Dragon("life_dragon", "Plump forest green dragon with gracefully folded wings that look like leaves.", life_options, "green", "life"),
    'egg': creature.Creature("egg", "Ostrich egg sized pearlescent egg. Glowing softly.", egg_options),
}

# Add Creatures to rooms

def add_creatures():
    room['outside'].creatures = [creature['lizard']]
    room['foyer'].creatures = [creature['lizard'], creature['mouse']]
    room['overlook'].creatures = [creature['lizard'], creature['ghost']]
    room['platform'].creatures = [creature['lizard'], creature['fire_dragon']]
    room['narrow'].creatures = [creature['lizard'], creature['mouse']]
    room['treasure'].creatures = [creature['lizard'], creature['bat'], creature['life_dragon']]
    room['top'].creatures = [creature['lizard'], creature['ice_dragon']]
    room['secret'].creatures = [creature['lizard'], creature['egg']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Define choices

def dir(choice):
    try:
        if choice[0] == "n":
            return "n_to"

        elif choice[0] == "e":
            return "e_to"

        elif choice[0] == "s":
            return "s_to"

        elif choice[0] == "w":
            return "w_to"

        elif choice[0] == "l":
            return "look"

        elif choice[0] == "i":
            return "inventory"

        elif choice[0] == "p":
            return ["pickup", choice[1]]

        elif choice[0] == "d":
            return ["drop", choice[1]]

        elif choice[0] == "a":
            return ["add", choice[1]]

        elif choice[0] == "u":
            return "uniquip"

        elif choice[0] == "t":
            return ["talk", choice[1]]

        elif choice[0] == "h":
            return "need_help"

        elif choice[0] == "q":
            return "quit"

        else:
            print("Please enter a valid choice.")

    except ValueError:
        print("Please enter a valid choice.")

def welcome():
    print(
        "\nWelcome to the Cave of Wonders! You are about to go on a MIGHTY QUEST FOR TREASUR--\n\nOkay. I can see you don't believe me. Let me rephrease...\n\nYou are about to go on a WHIRLWHIND OF ADVENTU--\n\nStill no, huh? You're hard to please. 🤔 Let me try once again...\n\nYou're about to embark on a FUN AND QUICK LITTLE ADVENTURE!!!!\n\n\nYou are faced with several rooms. You'll move by entering [n] to go North, [e] to East, [s] to go South, [w] to go West. You have other options as well, enter [h] to discover more, Oh Great Adventurer!\n\nYour task is to find the Treasure Room, but beware...not all may be as it seems!\n"
    )

def help_msg():
    print("\n---------------------------------------- \nMovement:\n [n] ... go North\n [e] ... go East\n [s] ... go South\n [w] ... go West\n\nItems:\n [l] ... (L)look around\n [i] ... inventory\n [p item] ... pick up item\n [d item] ... drop item\n\nCreatures:\n [t creature] ... talk with creature\n [] ... something\n\nOther:\n [h] ... help (obviously!)\n [q] ... quit the game\n---------------------------------------- \n")

def player():
    name = input("What is your name, oh brave and wise adventurer? \n --> ")

    print(f"\n\nYou are standing at the {room['outside'].title}. All around you is a desolate expanse of sand. {room['outside'].description}\n")

    global player
    player = Player(name, room["outside"])

def get_player_choice():
    player_choice = input(f"What would you like to do?\n --> ")
    print(f"--- {player.name} has entered: {player_choice} ---")
    lowered = player_choice.lower().split(" ")
    return dir(lowered)

def no_dir():
    print("There's nothing for you in that direction!")

def go_to_room(direction):
    player.change_room(room[direction.name])
    print(f"You have entered {player.cr.title}. {player.cr.description}")

def play():
    reset_room_items()
    add_creatures()
    playing = True
    while playing:
        player_choice = get_player_choice()

        # directions
        if player_choice == "n_to":
            if room[player.cr.name].n_to:
                direction = room[player.cr.name].n_to
                go_to_room(direction)
            else:
                no_dir()

        elif player_choice == "e_to":
            if room[player.cr.name].e_to:
                direction = room[player.cr.name].e_to
                go_to_room(direction)
            else:
                no_dir()

        elif player_choice == "s_to":
            if room[player.cr.name].s_to:
                direction = room[player.cr.name].s_to
                go_to_room(direction)
            else:
                no_dir()

        elif player_choice == "w_to":
            if room[player.cr.name].w_to:
                direction = room[player.cr.name].w_to
                go_to_room(direction)
            else:
                no_dir()

        # items
        elif player_choice == "look":
            print(room[player.cr.name].list_items())
            print(room[player.cr.name].list_creatures())

        elif player_choice == "inventory":
            print(player.inventory())

        elif player_choice[0] == "pickup":
            print(player.pickup(player_choice[1]))
            player.cr.picked_up(player_choice[1])

        elif player_choice[0] == "drop":
            print(player.drop(player_choice[1]))
            player.cr.dropped(player_choice[1])

        # elif player_choice[0] == "add":
        #     if player.weapon == None:
        #         player.weapon == player_choice[1]
        #         player.cr.picked_up(player_choice[1])
        #     else:
        #         print(f"You may only have one weapon at a time. Please unequip your {player.weapon.name} first.")

        # elif player_choice[0] == "unequip":
        #     if player.weapon == None:
        #         print("You have no weapon to unequip!")
        #     else:
        #         player.unequip()
        #         player.cr.dropped(player.weapon)

        # creatures
        elif player_choice[0] == "talk":
            print(creature[player_choice[1]].speak())
        
        # other options
        elif player_choice == "need_help":
            help_msg()

        elif player_choice == "invalid":
            print("That choice is currently unacceptable!")

        elif player_choice == "quit":
            print(f"Thank you for visiting the Cave of Wonders! I hope you'll adventure again with us soon!")
            playing = False
            exit()

welcome()
player()
play()
        

"""
- Creatures that talk. 
    - with randomized sayings?
- Couple - Few Extra rooms
- Rescue the dragon egg
- Ghost flies you to platform
- make platform description.
"""