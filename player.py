import random

from enum import Enum

class Role(Enum):
    MAFIA = "mafia"
    TOWN = "townsfolk"

class PlayerType(Enum):
    HUMAN = 0
    AI = 1

class Player:
    def __init__(self, name, role, alive=True, type=PlayerType.AI):
        self.name = name
        self.role = role
        self.alive = alive
        self.type = type
    
    def assign_role(self):
        if random.random() < 0.5:
            self.role = Role.MAFIA
        else:
            self.role = Role.TOWN
