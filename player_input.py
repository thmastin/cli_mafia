from player import Player

def pause_game():
    input("Press Enter to continue...")

def player_vote(human):
    if human.role is Role.MAFIA:
        mafia_kill = input("Type in 'Kill' followed by the plaher name to kill and pres Enter")
        split_kill = mafia_kill.split()
        if split_kill[0].lower() != "kill":
            print("Invalid input, you must start the command with 'Kill'.")
            player_vote(human)
        else:
            print(f"Player elects to kill {split_kill[1]}")

