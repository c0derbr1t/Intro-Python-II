from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'platform': Room("platform", "Distant Platform", """DESCRIPTION"""),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['platform']
room['platform'].s_to = room['overlook']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
        if choice == "n":
            return "n_to"

        elif choice == "e":
            return "e_to"

        elif choice == "s":
            return "s_to"

        elif choice == "w":
            return "w_to"

        elif choice == "h":
            return "need_help"

        elif choice == "q":
            return "quit"

        else:
            print("Please enter a valid choice.")

    except ValueError:
        print("Please enter a valid choice.")

playing = True

def welcome():
    print(
        "\nWelcome to the Cave of Wonders! You are about to go on a MIGHTY QUEST FOR TREASUR--\n\nOkay. I can see you don't believe me. Let me rephrease...\n\nYou are about to go on a WHIRLWHIND OF ADVENTU--\n\nStill no, huh? You're hard to please. 🤔 Let me try once again...\n\nYou're about to embark on a FUN AND QUICK LITTLE ADVENTURE!!!!\n\n\nYou are faced with several rooms. You'll move by entering [n] to go North, [e] to East, [s] to go South, [w] to go West. You have other options as well, enter [h] to discover more, Oh Great Adventurer!\n\nYour task is to find the Treasure Room, but beware...not all may be as it seems!\n"
    )

def help_msg():
    return "\n---------------------------------------- \nMovement:\n [n] ... go North\n [e] ... go East\n [s] ... go South\n [w] ... go West\n\nOther:\n [h] ... help (obviously!)\n [q] ... quit the game\n---------------------------------------- \n"

def player():
    name = input("What is your name, oh brave and wise adventurer? \n --> ")

    print(f"\n\nYou are standing at the {room['outside'].title}. All around you is a desolate expanse of sand. {room['outside'].description}\n")

    global player
    player = Player(name, room["outside"])

def get_player_choice():
    player_choice = input(f"{player.name}, What would you like to do?\n --> ")
    print(f"--- Player has entered: {player_choice} ---")
    lowered = player_choice.lower()
    return dir(lowered)

def play():
    while playing:
        player_choice = get_player_choice()

        # directions
        if player_choice == "n_to":
            if room[player.cr.name].n_to:
                direction = room[player.cr.name].n_to
                player.change_room(room[direction.name])
                print(f"You have entered {player.cr.title}. {player.cr.description}")
            else:
                print("There's nothing for you in that direction!")

        elif player_choice == "e_to":
            if room[player.cr.name].e_to:
                direction = room[player.cr.name].e_to
                player.change_room(room[direction.name])
                print(f"You have entered {player.cr.title}. {player.cr.description}")
            else:
                print("There's nothing for you in that direction!")

        elif player_choice == "s_to":
            if room[player.cr.name].s_to:
                direction = room[player.cr.name].s_to
                player.change_room(room[direction.name])
                print(f"You have entered {player.cr.title}. {player.cr.description}")
            else:
                print("There's nothing for you in that direction!")

        elif player_choice == "w_to":
            if room[player.cr.name].w_to:
                direction = room[player.cr.name].w_to
                player.change_room(room[direction.name])
                print(f"You have entered {player.cr.title}. {player.cr.description}")
            else:
                print("There's nothing for you in that direction!")

        elif player_choice == "need_help":
            print(help_msg())

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