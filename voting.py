import random
import ui

from player import Role, PlayerType
from player_input import player_vote_town

def ai_vote(voter_list, exclude_voter = None, exclude_role = None):
    valid_choices = []
    for voter in voter_list:
        if voter != exclude_voter and voter.role != exclude_role:
            valid_choices.append(voter)
    
    if valid_choices == []:
        raise ValueError("No valid choices")
    
    return random.choice(valid_choices)
    
    
def town_vote(voter, voter_list):
    return ai_vote(voter_list, voter)

def mafia_vote(voter, voter_list):
    return ai_vote(voter_list, voter, Role.MAFIA)

def day_vote(players_alive, players):
    votes = {}
    
    # HUman voting and add to the votes dictionary
    if players[0].alive is True:
        while True:
            human_vote = player_vote_town()
            found = False
            for player in players_alive:
                if human_vote.lower() == player.name.lower():
                    print(f"{players[0].name} votes for {player.name}")
                    votes[player.name] = 1
                    found = True
                    break
            if found:
                break
            ui.player_not_alive_error()
    for voter in players_alive:
        if voter.role == Role.TOWN and voter.type == PlayerType.AI:
            vote = town_vote(voter, players_alive)
            if vote.name in votes:
                votes[vote.name] = votes[vote.name] + 1
            else:
                votes[vote.name] = 1
            print(f"{voter.name} votes for {vote.name}")
        elif voter.type == PlayerType.AI:
            vote = mafia_vote(voter, players_alive)
            if vote.name in votes:
                votes[vote.name] = votes[vote.name] + 1
            else:
                votes[vote.name] = 1
 
            print(f"{voter.name} votes for {vote.name}")
    sorted_votes = sorted(votes.items(), key=lambda item: (-item[1], item[0]))
    print("Votes in order (highest to lowest):")
    for player_name, vote_count in sorted_votes:
        print(f"{player_name}: {vote_count} vote{'s' if vote_count != 1 else ''}")

    max_votes = max(votes.values())
    most_voted = []
    loser = None

    for vote in votes:
        if votes[vote] == max_votes:
            most_voted.append(vote)
    if len(most_voted) > 1:
        loser = random.choice(most_voted)
    else:
        loser = most_voted[0]
    print(f"Player getting the most votes: {loser}")
    for key in players_alive:
        if key.name == loser:
            return key


def night_vote(players_alive):
    eligible_targets = []
    for player in players_alive:
        if player.role is not Role.MAFIA:
            eligible_targets.append(player)
    if eligible_targets == []:
        return None
    else:
        return random.choice(eligible_targets)
      
            



