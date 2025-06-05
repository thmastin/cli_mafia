from player import Player
import random

def main():
    # Initialize a player

    player_1 = Player("Player 1", "Mafia")
    print(f"Player's Name: {player_1.name}")
    print(f"Player's Role: {player_1.role}")
    print(f"Is Player alive?: {player_1.alive}")

    #Kill player and test output

    player_1.alive = False

    print("")
    print("Player 1 has died!")
    print("")
    print(f"Player's Name: {player_1.name}")
    print(f"Player's Role: {player_1.role}")
    print(f"Is Player alive?: {player_1.alive}")

    #Generate a random number
    
          

if __name__ == "__main__":
    main()