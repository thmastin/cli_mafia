from player import Player

phase = "night"
players = []
players_alive = []
game_over = False
number_of_players = 8

def game_setup():
    mafia = 0
    townsfolk = 0
    for i in range(number_of_players):
        if mafia < 2:
            players.append(Player(f"Player {i + 1}", "townsfolk"))
            players[i].role = "mafia"
            mafia += 1
        else:
            players.append(Player(f"Player {i + 1}", "townsfolk"))
            townsfolk += 1

        print(mafia)
        print(townsfolk)
        print(players[i].name)
        print(players[i].role)