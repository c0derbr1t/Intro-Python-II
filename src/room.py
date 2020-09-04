# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """Create new Room instance"""
    def __init__(self, name, title, description):
        self.name = name
        self.title = title
        self.description = description
        self.items = []
        self.creatures = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):
        return f"Room({self.name}, {self.title}, {self.description})"

    def list_items(self):
        if len(self.items) > 0:
            itm_lst = ", "
            itms = [item.name for item in self.items]
            return f"This room contains {itm_lst.join(itms)}."
        else:
            return "This room is empty!"

    def list_creatures(self):
        if len(self.creatures) > 0:
            creature_lst = ", "
            creatures = [creature.name for creature in self.creatures]
            return f"This room contains {creature_lst.join(creatures)}."
        else:
            return "This room contains no creatures."

    def picked_up(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
        elif len(self.items) == 0:
            return "There is nothing to pick up here!"
        else:
            return f"You cannot pick up {item}, as it is not in this room."

    def dropped(self, item):
        self.items.append(item)