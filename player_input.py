from player import Player

def pause_game():
    input("Press Enter to continue...")

def player_vote_mafia():
    mafia_kill = input("Type in 'Kill' followed by the player name to kill and press Enter: ")
    split_kill = mafia_kill.split()
    print(split_kill)
    if split_kill[0].lower() != "kill":
        print("Invalid input, you must start the command with 'Kill'.")
        return player_vote_mafia()
    else:
        print(f"Player elects to kill {split_kill[1]}")
        return split_kill[1].lower()
    
def player_discuss():
    return input("Type in a player's name to accuse them of being Mafia and press Enter: ")

def player_vote_town():
    player_vote = []
    player_vote = input("Type in 'Vote' followed by the player name to vote for a player to kill and then press Enter: ").lower().split()
    print(player_vote)
    if player_vote == []:
        print("Invalid input, you must start with the command 'vote'. Try again!")
        return player_vote_town()
    if player_vote[0] != "vote":
        print("Invalid input, you must start with the command 'vote'. Try again!")
        return player_vote_town()
    print(f"Player votes to kill {player_vote[1]}")
    return player_vote[1]
    
        
