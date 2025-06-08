import random

from player import *
from voting import day_vote, night_vote

phase = "night"
players = []
players_alive = []
number_of_players = 8

def game_setup():
    # Make sure lists are empty
    players.clear()
    players.clear()
    
    # Determine the number of mafia (1/4 of players minimum 1)
    num_mafia = max(1, number_of_players // 4)
    
    # Create role list with num_mafia MAFIA and remaining TOWN
    roles = [Role.MAFIA] * num_mafia + [Role.TOWN] * (number_of_players - num_mafia)
    random.shuffle(roles)

    #Assign roles to players
    for i in range(number_of_players):
        new_player = Player(f"Player {i + 1}", roles[i])
        players.append(new_player)
        players_alive.append(new_player)

    #Debug: Print roles to verify
    for player in players:
        print(f"{player.name}: {player.role.value}")
        print(f"Total Mafia: {num_mafia} Total Townsfolk = {number_of_players - num_mafia}")
    
def game_cycle():
    mafia = 0
    townsfolk = 0
    game_over = False
    game_phase = "night"
    win = ""

    for i in range(len(players)):
        if players[i].role == Role.MAFIA:
            mafia += 1
        else:
            townsfolk += 1
        print(f"Total mafia: {mafia}")
        print(f"Total Townsfolk: {townsfolk}")
        print(f"Players Alive: {len(players_alive)}")    

    while game_over == False:
        if townsfolk > 0 and mafia <= len(players_alive):
            if game_phase == "night":
                print("It is night")
                townsfolk -= 1
                game_phase = "day"
                night_vote(players_alive)
            if game_phase == "day":
                print("It is day")
                game_phase = "night"
                day_vote(players_alive)                    
        else:
            print("Game Over")
            if mafia == 0:
                win = "Townsfolk"
            else:
                win = "Mafia"
            print(f"{win} have won the game!")
            game_over = True
            return
