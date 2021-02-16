from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
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

def dir(input):
    switcher = {
        "n": "n_to",
        "e": "e_to",
        "s": "s_to",
        "w": "w_to",
        "q": "quit"
    }
    return switcher.get(input, "Invalid Choice.")

def rm(i):
    switcher = {
        "Outside Cave Entrance": "outside",
        "Foyer": "foyer",
        "Grand Overlook": "overlook",
        "Narrow Passage": "narrow",
        "Treasure Chamber": "treasure"
    }
    return switcher.get(i, "That room does not exist.")

def welcome():
    print(
        "\nWelcome to Britt's Adventure! This is a quick little text-based game.\n\nYou are faced with several rooms. You'll move by entering [n] to go North, [e] to go East, [s] to go South, [w] to go West, or [q] to quit!\n\nYour task is to find the Treasure Room, then escape back outside to win!\n"
    )



def user():
    name = input("What is your name, adventurer?\n-->  ")
    global user 
    user = Player(name, room["outside"], "outside")

def get_user_choice():
    user_choice = input(f"\nWhich direction would you like to move, {user.name}?\n-->  ")
    return user_choice

def play():
    playing = True
    while playing:
        print(f"\nYou are standing in the {user.current_room.title}. {user.current_room.description}.")
        user_choice = get_user_choice()
        user_room_str = rm(user.current_room.title)
        user_room_title = user.current_room.title

        if user_choice == "n":
            direction = room[user_room_str].n_to
        elif user_choice == "e":
            direction = room[user_room_str].e_to
        elif user_choice == "s":
            direction = room[user_room_str].s_to
        elif user_choice == "w":
            direction = room[user_room_str].w_to
        elif user_choice == "q":
            direction = "quit"

        if direction:
            if direction == "quit":
                print("Thank you for playing Britt's Adventure!!!")
                playing = False
            else:
                new_rm = rm(direction.title)
                user.change_room(room[new_rm])
                print(f"\nYou walk through the doorway into {direction.title}.")
        else:
            if user_room_title == "Outside Cave Entrance":
                print("\nYou wander around in the open for a while, then return to the Outside Cave Entrance.")
            else:
                print("\nYou've ran into a wall! You might want to go a different direction...")
    
welcome()
user()
play()