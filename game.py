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
    players_alive.clear()
    
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
    game_phase = "night"
    night_count = 1
    day_count = 1

    # Set the total number of Mafia and Townsfolk
    for i in range(len(players)):
        if players[i].role == Role.MAFIA:
            mafia += 1
        else:
            townsfolk += 1
    
    while win_check(mafia, townsfolk) is False:
        if game_phase == "night":
            print(f"Night {night_count}:")
            townsfolk -= 1
            game_phase = "day"
            night_vote(players_alive)
            night_count += 1
        if game_phase == "day":
            print(f"Day {day_count}:")
            game_phase = "night"
            day_vote(players_alive)
            day_count += 1                    
    print("Game Over")
    print(f"{determine_winner(mafia)} have won the game!")
    return

def win_check(mafia, townsfolk):
    if townsfolk > 0 and mafia <= len(players_alive):
        return False
    else:
        return True

def determine_winner(mafia):
    if mafia == 0:
        return "Townsfolk"
    else:
        return "Mafia"
