import csv

def load_player_names():
    with open('data/player_names.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        player_names = []
        for line in csv_reader:
            player_names.append(line[0])
    return player_names

def load_vote_messages():
    with open('data/vote_messages.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        vote_messages = {}
        for line in csv_reader:
            vote_messages[line[0]] = line[1]
    return vote_messages

def load_discussion_messaages():
    with open("data/discussion_messages.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        discussion_messages = {}
        for line in csv_reader:
            discussion_messages[line[0]] = line[1]
    return discussion_messages

def load_maffia_kill_messages():
    with open("data/mafia_kill_messages.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        mafia_kill_messages = {}
        for line in csv_reader:
            mafia_kill_messages[line[0]] = line[1]
    return mafia_kill_messages


