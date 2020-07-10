from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """Create a new Player instance"""
    def __init__(self, name, room, rm_str):
        self.rm_str = rm_str
        self.current_room = room
        self.name = name
        self.items = []
        self.gold = 0

    def __str__(self):
        output = f"Name: {self.name}\n"
        room = f"Room: {self.current_room.title}\nDesc: {self.current_room.description}\n"
        if len(self.items) > 0:
            itm_str = ", "
            itms = [item.name for item in self.items]
            items = f"Items: {itm_str.join(itms)}"
        else:
            items = "None"
        return output + room + items

    def change_room(self, room): # expects room["room"]
        self.current_room = room
        
    def list_inventory(self):
        if len(self.items) > 0:
            itms = [item for item in self.items]
            itm_lst = ", "
            return f"You are holding {itm_lst.join(itms)}."
        else:
            return "You aren't holding anything!"
    
    def how_much_gold(self):
        if self.gold == 0:
            return f"Your💰 You have no gold!"
        return f"Your💰 {str(self.gold)}"

    def pickup_gold(self, amount):
        self.gold += int(amount)
        return f"Your💰 {str(self.gold)}"

    def drop_gold(self, amount):
        if self.gold - int(amount) < 0:
            new_amount = self.gold
            self.gold = 0
            return f"You could only drop {str(new_amount)}, as that is all you had.\n💰 {str(self.gold)}"
        self.gold -= int(amount)
        return f"Your💰 {str(self.gold)}"

    def pickup_item(self, item):
        check_tr_a = [item for item in self.items if item == "treasure_a"]
        check_tr_b = [item for item in self.items if item == "treasure_b"]
        if item == "treasure_a" and check_tr_b:
            return "You already have treasure_b. You can only pick up one Treasure. Choose wisely!"
        elif item == "treasure_b" and check_tr_a:
            return "You already have treasure_a. You can only pick up one Treasure. Choose wisely!"
        self.items.append(item)
        itms = [item for item in self.items]
        itm_str = ", "
        return f"You have picked up {item}. You currently hold {itm_str.join(itms)}."

    def drop_item(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
            itm_str = ", "
            itms = [item for item in self.items]
            return f"You have dropped {item}. You currently hold {itm_str.join(itms)}."
        elif len(self.items) == 0:
            return "You are not currently holding any items!"
        else:
            itm_str = ", "
            itms = [item for item in self.items]
            return f"You cannot drop this, as You do not currently hold {item}. You are holding {itm_str.join(itms)}."