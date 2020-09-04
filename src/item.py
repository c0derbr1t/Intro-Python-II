class Item:
    """Create basic Item instance"""
    def __init__(self, name, description):
        self.name = name

class Weapon(Item):
    def __init__(self, name, description, kind):
        super().__init__(name, description)
        self.kind = kind

class Magical_Item(Item):
    def __init__(self, name, description, kind):
        super().__init__(name, description)
        self.kind = kind

class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)