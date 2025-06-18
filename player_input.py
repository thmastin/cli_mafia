from player import Player

def pause_game():
    input("Press Enter to continue...")

def player_vote_mafia():
    mafia_kill = input("Type in 'Kill' followed by the plaher name to kill and press Enter: ")
    split_kill = mafia_kill.split()
    print(split_kill)
    if split_kill[0].lower() != "kill":
        print("Invalid input, you must start the command with 'Kill'.")
        player_vote_mafia()
    else:
        print(f"Player elects to kill {split_kill[1]}")
        return split_kill[1].lower()
    
def player_discuss():
    return input("Type in a player's name to accuse them of being Mafia and press Enter: ")
        
