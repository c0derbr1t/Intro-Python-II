# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """Create new Room instance"""
    def __init__(self, name, title, description):
        self.name = name
        self.title = title
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):
        return f"Room({self.name}, {self.title}, {self.description})"