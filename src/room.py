# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """Create a new Room instance"""
    def __init__(self, title, description, gold=0):
        self.title = title
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        self.gold = gold

    def list_items(self):
        if len(self.items) > 0:
            itm_lst = ", "
            itms = [item.name for item in self.items]
            return f"This room contains {itm_lst.join(itms)}."
        else:
            return "This room is empty."

    def how_much_gold(self):
        return f"Room💰 {str(self.gold)}"

    def gold_dropped(self, amount):
        self.gold += int(amount)
        return f"Room💰 {str(self.gold)}"

    def gold_picked_up(self, amount):
        if self.gold - int(amount) <0:
            new_amount = self.gold
            self.gold = 0
            return f"You could only pick up{str(new_amount)}, as that was all the gold available.\nRoom💰 {str(self.gold)}"
        else:
            self.gold -= int(amount)
            return f"Room💰 {str(self.gold)}"

    def item_picked_up(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
        elif len(self.items) == 0:
            return "There is nothing to pick up here!"
        else:
            itm_lst = ", "
            itms = [item.name for item in self.items]
            return f"You cannot pick up {item}, as it is not in this room. The items available are {itm_lst.join(itms)}."

    def item_dropped(self, item):
        self.items.append(item)
        return "You dropped something..."