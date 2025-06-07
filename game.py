from player import Player

phase = "night"
players = []
players_alive = []
number_of_players = 8

def game_setup():
    
    # Initialize players and assign roles
    mafia = 0
    townsfolk = 0
    for i in range(number_of_players):
        if mafia < 2:
            new_player = (Player(f"Player {i + 1}", "mafia"))
            players.append(new_player)
            mafia += 1
        else:
            new_player = Player(f"Player {i + 1}", "townsfolk")
            players.append(new_player)
            townsfolk += 1

    # Add starting players to alive
    for i in range(len(players)):
        alive_player = players[i]
        players_alive.append(alive_player)

def game_cycle():
    mafia = 0
    townsfolk = 0
    game_over = False
    game_phase = "night"

    for i in range(len(players)):
        if players[i].role == "mafia":
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
            if game_phase == "day":
                print("It is day")
                game_phase = "night"
                townsfolk -= 1
        else:
            print("Game Over")
            print(f"Mafia remaining: {mafia}")
            print(f"Townsfolk remaining: {townsfolk}")
            game_over = True
            return
