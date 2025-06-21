import csv

def load_player_names():
    with open('data/player_names.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        player_names = []
        for line in csv_reader:
            player_names.append(line[0])
    print(player_names)
    return player_names

