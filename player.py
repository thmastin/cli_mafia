import random

class Player:
    def __init__(self, name, role, alive=True):
        self.name = name
        self.role = role
        self.alive = alive
    
    def assign_role(self):
        if random.random() < 0.5:
            self.role = "mafia"
        else:
            self.role = "townsfolk"
