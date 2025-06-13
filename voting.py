import random

from player import Role

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

def day_vote(voter_list):
    votes = {}
    for voter in voter_list:
        if voter.role == Role.TOWN:
            vote = town_vote(voter, voter_list)
            if vote.name in votes:
                votes[vote.name] = votes[vote.name] + 1
            else:
                votes[vote.name] = 1
            print(f"{voter.name} votes for {vote.name}")
        else:
            vote = mafia_vote(voter, voter_list)
            if vote.name in votes:
                votes[vote.name] = votes[vote.name] + 1
            else:
                votes[vote.name] = 1
 
            print(f"{voter.name} votes for {vote.name}")
    print(f"Total votes: {votes}")


def night_vote(players_alive):
    eligible_targets = []
    for player in players_alive:
        if player.role is not Role.MAFIA:
            eligible_targets.append(player)
    return random.choice(eligible_targets)
      
            



