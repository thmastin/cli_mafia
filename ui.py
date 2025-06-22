import csv_handler
import random

MOON_ART = """ 🌙 """

SUN_ART = """ ☀️ """

# Print functions for the game setup phase of the game

def welcome_message():
    greeting_messages = csv_handler.load_greeting_messages()
    keys_list = list(greeting_messages.keys())
    random_key = random.choice(keys_list)
    message = greeting_messages[random_key]
    print(f"{message}")


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
    mafia_kill_messages = csv_handler.load_mafia_kill_messages()
    keys_list = list(mafia_kill_messages.keys())
    random_key = random.choice(keys_list)
    message = mafia_kill_messages[random_key]
    print(f"{message.format(target_name = target.name)}")

def town_kill_message(day_killed):
    town_kill_messages = csv_handler.load_town_kill_messages()
    keys_list = list(town_kill_messages.keys())
    random_key = random.choice(keys_list)
    message = town_kill_messages[random_key]
    print(f"{message.format(target_name = day_killed.name, target_role = day_killed.role.value)}")

def print_discussion(accused_players, count, game_phase):
    print(f"{game_phase.capitalize()} {count} Discussion")
    print("--------------------------------------")
    discussion_messages = csv_handler.load_discussion_messaages()
    keys_list = list(discussion_messages.keys())
    for player in accused_players:
        random_key = random.choice(keys_list)
        message = discussion_messages[random_key]
        print(f"{message.format(accuser_name = player[0], accused_name = player[1].capitalize())}")

# Input Error Messages

def mafia_input_error():
    print("You must enter a player's name that is a townsfolk and is still alive. Try again!")

def player_not_alive_error():
    print("You must type in a player name that is still alive. Try again!")

def invalid_kill_error():
    print("Invalid input, you must start the command with 'Kill'.")

def invalid_vote_error():
    print("Invalid input, you must start with the command 'vote'. Try again!")

def empty_player_name():
    print("ERROR: You must enter a name.")

def town_voting_header():
    print("--------------------------------------")
    print('The town begins voting...')
    print("--------------------------------------")

def player_mafia_kill(target):
    print(f"You elect to kill {target}")

def vote(voter_name, vote_name):
    vote_messages = csv_handler.load_vote_messages()
    keys_list = list(vote_messages.keys())
    random_key = random.choice(keys_list)
    message = vote_messages[random_key]

    print(f"{message.format(voter_name = voter_name, vote_name = vote_name)}")

def voting_results(sorted_votes, loser):
    print("--------------------------------------")
    print("Votes in order (highest to lowest)")
    print("--------------------------------------")
    for player_name, vote_count in sorted_votes:
        print(f"{player_name}: {vote_count} vote{'s' if vote_count != 1 else ''}")
    print("--------------------------------------")
    print(f"Player getting the most votes: {loser}")
    print("--------------------------------------")

# Player input messages

def prompt_pause():
    print('Press Etner to continue...')
    return input().strip

def prompt_mafia_kill():
    print("Type in 'Kill' followed by the player name to kill and press Enter: ")
    return input().strip()

def prompt_discuss():
    print("Type in a player's name to accuse them of being Mafia and press Enter: ")
    return input().strip()

def prompt_player_vote():
    print("Type in 'Vote' followed by the player name to vote for a player to kill and then press Enter: ")
    return input().strip()

def prompt_payer_name():
    print("Enter your name and press <Enter>:")
    return input().strip()

def player_name():
    while True:
        name = prompt_payer_name()
        if name != "":
            break
        else:
            empty_player_name()
    return name




       









