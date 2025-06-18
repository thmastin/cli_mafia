import random

from player import *
from voting import day_vote, night_vote
from player_input import pause_game, player_vote_mafia, player_discuss

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
    human_player = Player("Player1 - Human", role=roles[0], type=PlayerType.HUMAN)
    players.append(human_player)
    players_alive.append(human_player)
    for i in range(number_of_players - 1):
        new_player = Player(f"Player{i + 2}", roles[i + 1])
        players.append(new_player)
        players_alive.append(new_player)

    #Debug: Print roles to verify
    print(f"Total Mafia: {num_mafia} Total Townsfolk = {number_of_players - num_mafia}")
    for player in players:
        print(f"{player.name}: {player.role.value}")
    pause_game()
    
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
            target = None
            print(f"Night {night_count}:")
            print(f"Players Alive:")
            output_players_alive(players_alive)
            pause_game()
            if players[0].alive is True and players[0].role is Role.MAFIA:
                while True:
                    player_to_kill = player_vote_mafia()
                    for player in players_alive:
                        if player_to_kill == player.name.lower():
                            target = player
                    if target is not None and target.role is not Role.MAFIA:
                            break
                    print("You must enter a player's name that is a townsfolk and is still alive. Try again!")
            else:
                target = night_vote(players_alive)
            print(f"{target.name} was killed during the night")
            target.alive = False
            players_alive.remove(target)
            townsfolk -= 1
            night_count += 1
            game_phase = "day"

            update_players_alive(players)
            mafia, townsfolk = count_roles(players_alive)

            if win_check(mafia, townsfolk):
                print("Game Over")
                print(f"{determine_winner(mafia)} have won the game!")
                break
            pause_game()

        else: 
            print(f"Day {day_count}:")
            print(f"Players Alive:")
            output_players_alive(players_alive)
            game_phase = "night"
            pause_game()

            day_discuss(players_alive, day_count)
            pause_game()
            day_killed = day_vote(players_alive)
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
            pause_game()

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

    if players[0].alive is True:
        while True:
            human_accuse = player_discuss()
            found = False
            for player in players_alive:
                if human_accuse.lower() == player.name.lower():
                    print(f'Day {count} Discussion:')
                    print(f"{players[0].name} accuses {human_accuse}")
                    found = True
                    break
            if found:
                break
            print("You must type in a player name that is still alive. Try again!")

    for player in players_alive:
        if player.role is Role.TOWN:
            town_eligible.append(player)
    for player in players_alive:
        if player.role is Role.MAFIA and player.type == PlayerType.AI:
            print(f"{player.name} accuses {random.choice(town_eligible).name}")
        elif player.type == PlayerType.AI:
            print(f"{player.name} accuses {random.choice(players_alive).name}")
           