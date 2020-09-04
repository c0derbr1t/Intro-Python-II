import random

class Creature:
    """Create basic Creature instance"""
    def __init__(self, name, description, statements):
        self.name = name
        self.description = description
        self.statements = statements

    def speak(self):
        return random.choice(self.statements)

class Friendly(Creature):
    def __init__(self, name, description, statements, species):
        super().__init__(name, description, statements)
        self.species = species

class Grumpy(Creature):
    def __init__(self, name, description, statements, species):
        super().__init__(name, description, statements)
        self.species = species

    def attack(self):
        return "You will suffer for your insolence."

class Dragon(Creature):
    def __init__(self, name, description, statements, color, power):
        super().__init__(name, description, statements)
        self.color = color
        self.power = power

#Logic in adv.py instead of in here?
"""
    def attack(self):
        if self.power == fire:
            return 1
            # print(f"You are engulfed in a whirlwind of fire. Maybe, try not to anger {self.name} next time...")
            # playing = False
            # exit()  -> Platform
        elif self.power == ice:
            return 2
            # print("You are encased in everlasting ice. The Cave of Wonders is sealed for a Very Long Time. Maybe your ancestors will have better luck!")
            # playing = False
            # exit()  -> Mountain Top
        elif self.power == life:
            # Travel through the treasure room cave wall to a secret cavern find egg and treasure. pick up egg and treasure, 
            # Message about future with the special new species of dragon queen and wealth and if you help her grow her wealth she'll share it with you, if you do not she will eat you and your entire descendants.
            return 3
"""