import ui

from player import Player

def pause_game():
    input("Press Enter to continue...")

def player_vote_mafia():
    mafia_kill = input("Type in 'Kill' followed by the player name to kill and press Enter: ")
    split_kill = mafia_kill.split()
    print(split_kill)
    if len(split_kill) <= 1:
        return player_vote_mafia()
    if split_kill[0].lower() != "kill":
        ui.invalid_kill_error()
        return player_vote_mafia()
    else:
        ui.player_mafia_kill(split_kill[1])
        return split_kill[1].lower()
    
def player_discuss():
    return input("Type in a player's name to accuse them of being Mafia and press Enter: ")

def player_vote_town():
    player_vote = []
    player_vote = input("Type in 'Vote' followed by the player name to vote for a player to kill and then press Enter: ").lower().split()
    print(player_vote)
    if player_vote == []:
        ui.invalid_vote_error()
        return player_vote_town()
    if player_vote[0] != "vote":
        ui.invalid_vote_error()
        return player_vote_town()
    return player_vote[1]
    
        
