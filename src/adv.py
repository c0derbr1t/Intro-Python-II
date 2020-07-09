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

def welcome():
    print(
        "\nWelcome to Britt's Adventure! This is a quick little text-based game.\n\nYou are faced with several rooms. You'll move by entering 'n' to go North, 'e' to go East, 's' to go South, and 'w' to go West!\n\nYour task is to find the Treasure Room, then escape back outside to win!\n"
    )

def user():
    name = input("What is your name, adventurer?\n-->  ")
    global user 
    user = Player(name, room["outside"], "outside")

def play():
    if user.rm_str == "outside":
        print(f"You are {user.room[0]}. {user.room[1]}. ")
        user_choice = input(f"Which direction would you like to move, {user.name}?\n-->  ")
        # TODO: Figure out logic for changing rooms.
        if user_choice == "n":
            new_room = room[user.rm_str].n_to
            print(new_room)
            # user.change_room(f"{user_choice}_to")
    
# def play():
#     if user.room != "treasure":
#         description = textwrap.wrap(user.room[description], width=50)
#         title = user.room[title]
#         print(f"You are currently in the {title}.\n")
#         print(f"{description}\n")
#         user_choice = input(f"{user.name}, what would you like to do?\n-->  ")
#         if user_choice === "n" or user_choice == "e" or user_choice == "s" or user_choice == "w":
#             pass
#         else:
#             print("That's not a valid choice. Please enter 'n', 'e', 'w', or 's'!")
#             print("You've ran into a wall! You might want to go a different direction...")
    
welcome()
user()
play()
print(user)
print(user.rm_str)
print(user.room)
# play()
