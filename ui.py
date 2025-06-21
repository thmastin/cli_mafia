
# Print functions for the game setup phase of the game

def welcome_message():
    print("Hello! Let's play some mafia!")

def print_players_roles(players):
    print(f"Players Roles:")
    print("--------------------------------------")
    for player in players:
        print(f"{player.name}: {player.role.value}")

def print_human_role(players):
    print(f"You are {players[0].role.value}")

def end_of_game(winner, players):
    print("Game Over!")
    print(f"{winner} have won the game!")
    print(f"The players roles were:")
    print("---------------------------------------")
    print_players_roles(players)