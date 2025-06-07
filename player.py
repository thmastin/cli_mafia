import random

from enum import Enum

class Role(Enum):
    MAFIA = "mafia"
    TOWN = "townsfolk"

class Player:
    def __init__(self, name, role, alive=True):
        self.name = name
        self.role = role
        self.alive = alive
    
    def assign_role(self):
        if random.random() < 0.5:
            self.role = Role.MAFIA
            print(self.role)
        else:
            self.role = Role.TOWN
