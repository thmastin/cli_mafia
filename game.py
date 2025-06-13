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
    print(f"Total Mafia: {num_mafia} Total Townsfolk = {number_of_players - num_mafia}")
    for player in players:
        print(f"{player.name}: {player.role.value}")
    
def game_cycle():
    game_phase = "night"
    night_count = 1
    day_count = 1

    while True:
        update_players_alive(players)
        mafia, townsfolk = count_roles(players_alive)

        if win_check(mafia, townsfolk):
            print("Game Over")
            print(f"{determine_winner(mafia)} have won the game!")
            break

        if game_phase == "night":
            print(f"Night {night_count}:")
            print(f"Players Alive:")
            output_players_alive(players_alive)
            town_killed = night_vote(players_alive)
            print(f"{town_killed.name} was killed last night")
            town_killed.alive = False
            players_alive.remove(town_killed)
            townsfolk -= 1
            night_count += 1
            game_phase = "day"

            update_players_alive(players)
            mafia, townsfolk = count_roles(players_alive)

            if win_check(mafia, townsfolk):
                print("Game Over")
                print(f"{determine_winner(mafia)} have won the game!")
                break

        else: 
            print(f"Day {day_count}:")
            print(f"Players Alive:")
            output_players_alive(players_alive)
            game_phase = "night"
            day_discuss(players_alive, day_count)
            day_vote(players_alive)
            day_killed = random.choice(players_alive)
            day_killed.alive = False
            players_alive.remove(day_killed)
            print(f"{day_killed.name} was killed, they were {day_killed.role.value}")
            if day_killed.role is Role.MAFIA:
                mafia -= 1
            else:
                townsfolk -= 1
            day_count += 1

            update_players_alive(players)
            mafia, townsfolk = count_roles(players_alive)

            if win_check(mafia, townsfolk):
                print("Game Over")
                print(f"{determine_winner(mafia)} have won the game!")
                break

def win_check(mafia, townsfolk):
    if mafia == 0 or mafia >= townsfolk:
        return True
    else:
        return False

def determine_winner(mafia):
    if mafia == 0:
        return "Townsfolk"
    else:
        return "Mafia"
    
def output_players_alive(players_alive):
    for player in players_alive:
        print(player.name)

def update_players_alive(players):
    players_alive.clear()
    for player in players:
        if player.alive is True:
            players_alive.append(player)

def count_roles(players_alive):
    mafia = 0
    townsfolk = 0

    for player in players_alive:
        if player.role is Role.MAFIA:
            mafia += 1
        else:
            townsfolk += 1
    
    return mafia, townsfolk

def day_discuss(players_alive, count):
    town_eligible = []
    for player in players_alive:
        if player.role is Role.TOWN:
            town_eligible.append(player)
    print(f'Day {count} Discussion:')
    for player in players_alive:
        if player.role is Role.MAFIA:
            print(f"{player.name} accuses {random.choice(town_eligible).name}")
        else:
            print(f"{player.name} accuses {random.choice(players_alive).name}")
           