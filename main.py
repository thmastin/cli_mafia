from player import Player
from game import *
from setup import game_setup
import csv_handler

def main():
    players, players_alive = game_setup()  
    game_cycle(players, players_alive)
    
if __name__ == "__main__":
    main()