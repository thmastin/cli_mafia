import random
from player import Role, Player, PlayerType

def assign_roles(num_players, num_mafia):
    players= []
    players_alive = []

    #Create role list with num_mafia MAFIA and remaining TOWN
    roles = [Role.MAFIA] * num_mafia + [Role.TOWN] * (num_players - num_mafia)
    random.shuffle(roles)

    # Assign roles to players
    human_player = Player("Player1 - Human", role=roles[0], type=PlayerType.HUMAN)
    players.append(human_player)
    players_alive.append(human_player)
    for i in range(num_players - 1):
        new_player = Player(f"Player{i + 2}", roles[i + 1])
        players.append(new_player)
        players_alive.append(new_player)
    
    print(players_alive)

    return players, players_alive
