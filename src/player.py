# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """Create a new Player instance"""
    def __init__(self, name, room):
        self.name = name
        self.cr = room

    def __repr__(self):
        return f"Player({self.name}, {self.cr}"

    def change_room(self, room):
        self.cr = room