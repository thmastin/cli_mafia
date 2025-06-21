import random
import ui

from player import Role, Player, PlayerType
from player_input import pause_game


def game_setup():
    number_of_players = 8
  
    # Welcome the player to the game
    ui.welcome_message()
    pause_game()

    # Determine the number of mafia (1/4 of players minimum 1)
    num_mafia = max(1, number_of_players // 4)
    
    players, players_alive = assign_roles(number_of_players, num_mafia)
    
    # Tell the human player what their role is
    ui.print_human_role(players)
    pause_game()

    if players[0].role is Role.MAFIA:
        ui.print_players_roles(players)
        pause_game()

    return players, players_alive

def assign_roles(num_players, num_mafia):
    players= []
    players_alive = []

    #Create role list with num_mafia MAFIA and remaining TOWN
    roles = [Role.MAFIA] * num_mafia + [Role.TOWN] * (num_players - num_mafia)
    random.shuffle(roles)

    # Assign roles to players
    human_player = Player(ui.player_name(), role=roles[0], type=PlayerType.HUMAN)
    players.append(human_player)
    players_alive.append(human_player)
    for i in range(num_players - 1):
        new_player = Player(f"Player{i + 2}", roles[i + 1])
        players.append(new_player)
        players_alive.append(new_player)

    return players, players_alive
