import unittest

from game import *

class TestGame(unittest.TestCase):
    def test_player_count(self):
        game_setup()
        self.assertEqual(len(players), 8)
        
    def test_player_role_count(self):
        mafia_count = 0
        townsfolk_count = 0
        for i in range(len(players)):
            if players[i].role == Role.MAFIA:
                mafia_count += 1
            if players[i].role == Role.TOWN:
                townsfolk_count += 1
        self.assertEqual(mafia_count, 2)
        self.assertEqual(townsfolk_count, 6)

    def test_player_names(self):
        for i in range(len(players)):
            self.assertEqual(players[i].name, f"Player {i + 1}")

    def test_players_alive_initial(self):
        self.assertEqual(len(players_alive), 8)

    def test_players_equality(self):
        for i in range(len(players)):
            self.assertEqual(players[i], players_alive[i]) 
        

if __name__ == '__main__':
    unittest.main()