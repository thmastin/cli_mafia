from player import Player

phase = "night"
players = []
players_alive = []
game_over = False
number_of_players = 8

def game_setup():
    
    # Initialize players and assign roles
    mafia = 0
    townsfolk = 0
    for i in range(number_of_players):
        if mafia < 2:
            new_player = (Player(f"Player {i + 1}", "townsfolk"))
            players.append(new_player)
            players[i].role = "mafia"
            mafia += 1
        else:
            new_player = Player(f"Player {i + 1}", "townsfolk")
            players.append(new_player)
            townsfolk += 1

    # Add starting players to alive
    for i in range(len(players)):
        alive_player = players[i]
        players_alive.append(alive_player)
