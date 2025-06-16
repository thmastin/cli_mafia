from player import Player

def pause_game():
    input("Press Enter to continue...")

def player_vote(human):
    if human.role is Role.MAFIA:
        maifa_kill = input("Type in 'Kill' followed by the plaher name to kill and pres Enter")
        
