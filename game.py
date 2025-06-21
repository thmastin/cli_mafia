import random
import ui

from player import *
from voting import day_vote, night_vote
from player_input import pause_game, player_vote_mafia,player_discuss

  
def game_cycle(players, players_alive):
    game_phase = "night"
    count = 1

    while True:
        update_players_alive(players, players_alive)
        mafia, townsfolk = count_roles(players_alive)

        if win_check(mafia, townsfolk):
            winner = determine_winner(mafia)
            ui.end_of_game(winner, players)
            pause_game()
            break

        if game_phase == "night":
            target = None
            ui.print_game_phase(game_phase, count)
            ui.print_players_alive(players_alive)
            pause_game()
            if players[0].alive is True and players[0].role is Role.MAFIA:
                while True:
                    player_to_kill = player_vote_mafia()
                    for player in players_alive:
                        if player_to_kill == player.name.lower():
                            target = player
                    if target is not None and target.role is not Role.MAFIA:
                            break
                    ui.mafia_input_error()
            else:
                target = night_vote(players_alive)
            ui.mafia_kill_message(target)
            target.alive = False
            players_alive.remove(target)
            townsfolk -= 1
            game_phase = "day"

            update_players_alive(players, players_alive)
            mafia, townsfolk = count_roles(players_alive)

            if win_check(mafia, townsfolk):
                winner = determine_winner(mafia)
                ui.end_of_game(winner, players)
                pause_game()
                break
            pause_game()

        else: 
            ui.print_game_phase(game_phase, count)
            ui.print_players_alive(players_alive)
            game_phase = "night"
            pause_game()

            day_discuss(players, players_alive, count)
            pause_game()
            day_killed = day_vote(players_alive, players)
            day_killed.alive = False
            players_alive.remove(day_killed)
            ui.town_kill_message(day_killed)
            if day_killed.role is Role.MAFIA:
                mafia -= 1
            else:
                townsfolk -= 1
            count += 1

            update_players_alive(players, players_alive)
            mafia, townsfolk = count_roles(players_alive)

            if win_check(mafia, townsfolk):
                winner = determine_winner(mafia)
                ui.end_of_game(winner, players)
                pause_game()
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
    
def update_players_alive(players, players_alive):
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

def day_discuss(players, players_alive, count):
    town_eligible = []
    accused_players = []

    if players[0].alive is True:
        while True:
            human_accuse = player_discuss()
            found = False
            for player in players_alive:
                if human_accuse.lower() == player.name.lower():
                    accused = (players[0].name, human_accuse)
                    accused_players.append(accused)
                    found = True
                    break
            if found:
                break
            ui.player_not_alive_error()

    for player in players_alive:
        if player.role is Role.TOWN:
            town_eligible.append(player)
    for player in players_alive:
        if player.role is Role.MAFIA and player.type == PlayerType.AI:
            possible_targets = [p for p in town_eligible if p != player]
            accused = (player.name, random.choice(possible_targets).name)
            accused_players.append(accused)
        elif player.type == PlayerType.AI:
            possible_targets = [p for p in players_alive if p != player]
            accused = (player.name,random.choice(possible_targets).name)
            accused_players.append(accused)
    ui.print_discussion(accused_players, count, "Day")
           