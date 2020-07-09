from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, rm_str):
        self.rm_str = rm_str
        self.room = [room.title, room.description]
        self.name = name
        self.items = []

    def __str__(self):
        output = f"Name: {self.name}\n"
        room = f"Room: {self.room[0]}\nDesc: {self.room[1]}\n"
        if len(self.items) > 0:
            itm_str = ", "
            items = f"Items: {itm_str.join(self.items)}"
        else:
            items = "None"
        return output + room + items

    def change_room(self, room): # expects room["room"]
        if self.room[rm_str].dir == None:
            print("You've ran into a wall! You might want to go a different direction...")
        else:
            self.room = self.room.dir

    def list_inventory(self):
        print(f"You are holding {str(self.items)}.")

    def pickup_item(self, item):
        self.items.append(item)
        print(f"You have dropped {item}. You currently hold {str(self.items)}")

    def drop_item(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
        elif len(self.items) == 0:
            print("You are not currently holding any items!")
        else:
            print(f"You cannot drop this, as You do not currently hold {item}. You are holding {str(self.items)}")