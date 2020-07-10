from room import Room
from player import Player
import item
import textwrap

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", 0),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", 50),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", 100),

    'platform': Room("Distant Platform", "You fly across the chasm faster than you could even imagine, the shadowy depths blurring below you! You land and the rock is scarred with scorch marks, gouges, and 🩸SO MUCH BLOOD🩸! It feels ominous....and...THERE'S NO WAY OUT! You spend the rest of your short life on this platform. Everything fades to gray..."),
    ## future end to description:  maybe you should head back to the cave?

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", 100),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! At first it appears that it has already been completely emptied by earlier adventurers. The only exit is to the south.", 500),
}

# Create items
# worth -> "nothing", "a little", "medium", "a lot", "woah..."
# age -> "new", "baby", "child", "young adult", "adult", "elderly", "super old", "ancient"
baby_rat = item.Living("rat_a", "small", "nonviolent", "baby")
rat = item.Living("rat_b", "medium", "mild", "adult")
angry_rat = item.Living("rat_c", "large", "angry", "super old")
bird = item.Living("bird", "small", "timid", "young adult")
old_ghost = item.Living("ghost_a", "medium", "annoyed", "ancient")
new_ghost = item.Living("ghost_b", "small", "confused", "new")
angry_ghost = item.Living("ghost_c", "large", "angry", "super old")
vase = item.Valuable("vase", "small", "blue", "a lot")
sm_silver_coin = item.Valuable("coin_a", "small", "silver", "woah...")
md_gold_coin = item.Valuable("coin_b", "medium", "gold", "a little")
sm_skull = item.Valuable("sm_skull", "small", "bone", "a little")
weird_skull = item.Valuable("weird_skull", "huge", "bone", "woah...")
skull = item.Valuable("skull", "medium", "bone", "a little")
rock = item.Item("Rock", "medium")
dust = item.Item("Dust", "tiny")
feather = item.Item("Feather", "large")

a_treasure = item.Treasure("treasure_a", "small", "priceless", "💎 A plain chest, but when it is opened it is overflowing with gems, coins, jewelry, and unidentifiable wonders. Surprisingly, it seems to weigh nothing!")
b_treasure = item.Treasure("treasure_b", "huge", "a little", "💎 A beautiful chest, encrusted with jewels. However, upon closer inspection, everything on the inside and outside is fake!")
bonus_treasure = item.Treasure("bonus_treasure", "medium", "nearly priceless", "💎🩸💎 A bloodied chest, filled with nearly priceless treasure that is also covered in blood! 🩸")

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


# Add items to the rooms
def reset_room_items():
    room["outside"].items = []
    room["foyer"].items = []
    room["overlook"].items = []
    room["platform"].items = []
    room["narrow"].items = []
    room["treasure"].items = []
    room["outside"].items = [rock, rock, rock]
    room["foyer"].items = [skull, md_gold_coin]
    room["overlook"].items = [feather, bird, dust, old_ghost]
    room["platform"].items = [weird_skull, bonus_treasure]
    room["narrow"].items = [md_gold_coin, sm_silver_coin, skull, rat]
    room["treasure"].items = [skull, baby_rat, angry_rat, rat, weird_skull, sm_skull, dust, a_treasure, b_treasure]

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

# handle available inputs
def dir(input):
    switcher = {
        "h": "need_help",
        "c": "change",
        "n": "n_to",
        "e": "e_to",
        "s": "s_to",
        "w": "w_to",
        "l": "look",
        "g": "gold",
        "$": "my_gold",
        "i": "inventory",
        "p": "pickup",
        "d": "drop",
        "q": "quit"
    }

    return switcher.get(input.lower(), "invalid")

# handle room names
def rm(i):
    switcher = {
        "Outside Cave Entrance": "outside",
        "Foyer": "foyer",
        "Grand Overlook": "overlook",
        "Distant Platform": "platform",
        "Narrow Passage": "narrow",
        "Treasure Chamber": "treasure"
    }
    return switcher.get(i, "That room does not exist.")

playing = True
def welcome():
    reset_room_items()
    print(
        "\nWelcome to Britt's Adventure! This is a quick little text-based game.\n\nYou are faced with several rooms. You'll move by entering [n] to go North, [e] to go East, [s] to go South, [w] to go West. There are other options as well, just enter [h] for controls. 😁\n\nYour task is to find the Treasure Room, then escape back outside to win!\n"
    )

def help_msg():
    return "\n\nMovement:\n[n] --> go North\n[e] --> go East\n[s] --> go South\n[w] --> go West\n\nActions:\n[l] --> look to see what is in the room\n[g] --> check room for gold\n[$] --> check your gold\n[i] --> view your inventory\n[p 'item_name'] --> pick up an item\n[d 'item_name'] --> drop an item\n[p gold #] --> pickup an amount of gold\n[d gold #] --> drop an amount of gold\n\nOther:\n[c 'player_name'] --> change your player name\n[q] --> quit the game"

def user():
    name = input("What is your name, adventurer?\n-->  ")
    global user 
    user = Player(name, room["outside"], "outside")
    print()

def get_user_choice():
    print(f"\nYou are standing in the {user.current_room.title}.\n")
    print(f"You look around. {user.current_room.description}\n")
    user_choice = input(f"\nWhat would you like to do, {user.name}?\n-->  ")
    lower = user_choice.lower()
    split_input = lower.split(" ")
    if len(split_input) == 1:
        return dir(lower)
    elif len(split_input) == 2:
        return [dir(split_input[0]), split_input[1]]
    elif len(split_input) == 3:
        return [dir(split_input[0]), split_input[1], int(split_input[2])]

def play():
    playing = True
    instruction = "You can't do that yet!"
    while playing:
        
        user_choice = get_user_choice()
        user_room_str = rm(user.current_room.title)
        user_room_title = user.current_room.title

        # set the task to complete
        if user_choice == "n_to":
            instruction = room[user_room_str].n_to
        elif user_choice == "e_to":
            instruction = room[user_room_str].e_to
        elif user_choice == "s_to":
            instruction = room[user_room_str].s_to
        elif user_choice == "w_to":
            instruction = room[user_room_str].w_to

        elif user_choice == "look":
            instruction = room[user_room_str].list_items()
        elif user_choice == "inventory":
            instruction = user.list_inventory()
        elif user_choice == "gold":
            rm_gold = room[user_room_str].gold_dropped(0)
            instruction = rm_gold 
        elif user_choice == "my_gold":
            instruction = user.drop_gold(0)
        elif user_choice[0] == "pickup":
            if user_choice[1] == "gold":
                rm_gold = room[user_room_str].gold_picked_up(user_choice[2])
                user_gold = user.pickup_gold(user_choice[2])
                instruction = rm_gold + " | " + user_gold
            else:
                room[user_room_str].item_picked_up(user_choice[1])
                instruction = user.pickup_item(user_choice[1])
        elif user_choice[0] == "drop":
            if user_choice[1] == "gold":
                rm_gold = room[user_room_str].gold_dropped(user_choice[2])
                user_gold = user.drop_gold(user_choice[2])
                instruction = rm_gold + " | " + user_gold
            else:
                room[user_room_str].item_dropped(user_choice[1])
                instruction = user.drop_item(user_choice[1])

        elif user_choice[0] == "change":
            user.name = user_choice[1]
            instruction = user.name
        elif user_choice == "need_help":
            instruction = help_msg()
        elif user_choice == "quit":
            instruction = "quit"

        elif user_choice == "invalid":
            instruction = "That choice is currently unacceptable."
        
        # handle the task
        if instruction:
            if instruction == "quit":
                print("Thank you for playing Britt's Adventure!!!")
                playing = False
            elif user_choice == "look":
                print(instruction)
            elif user_choice == "inventory":
                print(instruction)
            elif user_choice == "gold":
                print(instruction)
            elif user_choice == "my_gold":
                print(instruction)
            elif user_choice[0] == "pickup":
                print(instruction)
            elif user_choice[0] == "drop":
                print(instruction)
            elif user_choice[0] == "change":
                print(instruction)
            elif user_choice == "need_help":
                print(instruction)
            elif user_choice == "invalid":
                print(instruction)

            else:
                new_rm = rm(instruction.title)
                if new_rm == "platform" and "feather" in user.items:
                    user.change_room(room["platform"])
                    print(room["platform"].description)
                    print("Your eyes close...\n\n\n\nYou are standing in front of a cave...how did you get here?\n\n\n")
                    user.change_room(room["outside"])
                elif new_rm == "platform" and "feather" not in user.items:
                    print("There must be a way to get there...I wonder what it is?")
                elif new_rm == "outside" and ("treasure_a" in user.items):
                    if "bonus_treasure" in user.items:
                        print(f"You found the bonus treasure! You look at it and see:\n{bonus_treasure.description}. Woah...this sounds dangerous!")
                    print(f"You look at the treasure you found...You see:\n {a_treasure.description}. You are elated!")
                    print("\n\nYOU'VE WON!!!! You have escaped the cave with the treasure!\n\nYou're so excited, but your vision begins to get hazy. Why are you here? What are you doing in front of this cave...\n\n\n")
                    user.change_room(room["outside"])
                    user.items = []
                elif new_rm =="outside" and ("treasure_b" in user.items):
                    if "bonus_treasure" in user.items:
                        print(f"You found the bonus treasure! You look at it and see:\n{bonus_treasure.description}. Woah...this sounds dangerous!")
                    print(f"You look at the treasure you found...You see:\n{b_treasure.description}. You are so disappointed!")
                    
                    print("\n\nYOU'VE WON!!!! You have escaped the cave with the treasure!\n\nYou're so excited, but your vision begins to get hazy. Why are you here? What are you doing in front of this cave...\n\n\n")
                    user.change_room(room["outside"])
                    user.items = []
                else:
                    user.change_room(room[new_rm])
                    # print(f"\nYou walk through the doorway into {instruction.title}.")
        else:
            if user_room_title == "Outside Cave Entrance":
                print("\nYou wander around in the open for a while, then return to the Outside Cave Entrance.")
            else:
                print("\nYou've ran into a wall! You might want to go a different direction...")
    
welcome()
user()
play()