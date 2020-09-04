# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """Create a new Player instance"""
    def __init__(self, name, room):
        self.name = name
        self.cr = room
        self.items = []
        self.weapon = None
        self.egg = False

    def __str__(self):
        return f"\nName: {self.name}\nRoom: {self.cr.title}\nItems: {len(self.items)}"

    def __repr__(self):
        return f"Player({self.name}, {self.cr}"

    def change_room(self, room):
        self.cr = room

    def inventory(self):
        if len(self.items) > 0:
            itms = [item for item in self.items]
            itm_str = ", "
            return f"You are holding {itm_str.join(itms)}."
        else:
            return "You aren't holding anything!"

    def pickup(self, item):
        self.items.append(item)
        itms = [item for item in self.items]
        itm_str = ", "
        return f"You have picked up {item}. You currently hold {itm_str.join(itms)}."

    def drop(self, item):
        if len(self.items) > 1 and item in self.items:
            self.items.remove(item)
            itms = [item for item in self.items]
            itm_str = ", "
            return f"You have dropped {item}. You currently hold {itm_str.join(itms)}."
        elif len(self.items) == 1 and item in self.items:
            self.items.remove(item)
            itms = [item for item in self.items]
            item_str = ", "
            return f"You have dropped {item}, and are now holding no items."
        elif len(self.items) == 0:
            return "You are not currently holding any items!"
        else:
            itm_str = ", "
            itms = [item for item in self.items]
            return f"You cannot drop this, as You do not currently hold {item}. You are holding {itm_str.join(itms)}."

    def equip(self, weapon):
        if self.weapon == None:
            self.weapon = weapon
            return f"You have equiped the {self.weapon.name} as your weapon. {self.weapon.description}"
        else:
            return f"You may only have one weapon at a time. Please unequip your {self.weapon.name} first."
    
    def unequip(self):
        self.weapon = None
        return f"You have unequipped your weapon."