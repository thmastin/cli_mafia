MOON_ART = """ 🌙 """

SUN_ART = """ ☀️ """

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

def print_game_phase(game_phase, count):
    if game_phase == "night":
        print(f"""
{MOON_ART}
Night {count}
        """)
    else:  # game_phase == "day"
        print(f"""
{SUN_ART}
Day {count}
        """)

def print_players_alive(players_alive):
    print("Players still living")
    print("--------------------------------------")
    for player in players_alive:
        print(f"{player.name}")

def mafia_kill_message(target):
    print(f"{target.name} was killed by the mafia during the night.")

def town_kill_message(day_killed):
    print(f"{day_killed.name} was killed, they were {day_killed.role.value}")

def print_discussion(accused_players, count, game_phase):
    print(f"{game_phase.capitalize()} {count} Discussion")
    print("--------------------------------------")
    for player in accused_players:
        print(f"{player[0]} accuses {player[1]}")

def mafia_input_error():
    print("You must enter a player's name that is a townsfolk and is still alive. Try again!")

def player_not_alive_error():
    print("You must type in a player name that is still alive. Try again!")

def town_voting_header():
    print("--------------------------------------")
    print('The town begins voting...')
    print("--------------------------------------")

def vote(voter_name, vote_name):
    print(f"{voter_name} votes to kill {vote_name}")

def voting_results(sorted_votes, loser):
    print("--------------------------------------")
    print("Votes in order (highest to lowest)")
    print("--------------------------------------")
    for player_name, vote_count in sorted_votes:
        print(f"{player_name}: {vote_count} vote{'s' if vote_count != 1 else ''}")
    print("--------------------------------------")
    print(f"Player getting the most votes: {loser}")
    print("--------------------------------------")




       









