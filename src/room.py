# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def list_items(self):
        print(f"This room contains {str(self.items)}.")

    def item_picked_up(self, item):
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
        elif len(self.items) == 0:
            print("There is nothing to pick up here!")
        else:
            print(f"You cannot pick up {item}, as it is not in this room. The items available are {str(self.items)}.")

    def item_dropped(self, item):
        self.items.append(item)
        print(f"{item} has been dropped in this room.")