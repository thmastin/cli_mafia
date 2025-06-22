import ui

from player import Player

def pause_game():
    ui.prompt_pause()

def player_vote_mafia():
    mafia_kill = ui.prompt_mafia_kill()
    split_kill = mafia_kill.split()
    if len(split_kill) <= 1:
        return player_vote_mafia()
    if split_kill[0].lower() != "kill":
        ui.invalid_kill_error()
        return player_vote_mafia()
    else:
        ui.player_mafia_kill(split_kill[1])
        return split_kill[1].lower()
    
def player_discuss():
    return ui.prompt_discuss()

def player_vote_town():
    player_vote = []
    player_vote = ui.prompt_player_vote().lower().split()
    if len(player_vote) < 2:
        ui.invalid_vote_error()
        return player_vote_town()
    if player_vote[0] != "vote":
        ui.invalid_vote_error()
        return player_vote_town()
    return player_vote[1]

def player_count():
    while True:
        try:
            player_number = int(ui.prompt_player_number())
            break
        except:
            ui.invalid_player_number()
    return player_number

    
        
