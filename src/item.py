class Item:
    """Create basic Item instance"""
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Living(Item):
    def __init__(self, name, size, disposition, age):
        super().__init__(name, size)
        self.disposition = disposition
        self.age = age

class Valuable(Item):
    def __init__(self, name, size, color, worth):
        super().__init__(name, size)
        self.color = color
        self.worth = worth 

class Treasure(Item):
    def __init__(self, name, size, worth, description):
        super().__init__(name, size)
        self.worth = worth
        self.description = description