from enum import Enum

class Role(Enum):
    MAFIA = "mafia"
    TOWN = "townsfolk"

class PlayerType(Enum):
    HUMAN = 0
    AI = 1

class Player:
    def __init__(self, name, role=None, alive=True, type=PlayerType.AI):
        self.name = name
        self.role = role
        self.alive = alive
        self.type = type
   
