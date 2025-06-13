import unittest
from game import *
from player import Player, Role, PlayerType
from voting import day_vote, night_vote, town_vote, mafia_vote, ai_vote
from contextlib import contextmanager
from io import StringIO
import sys

@contextmanager
def captured_output():
    new_out = StringIO()
    old_out = sys.stdout
    sys.stdout = new_out
    try:
        yield new_out
    finally:
        sys.stdout = old_out

class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game state before each test."""
        game_setup()

    def tearDown(self):
        """Clean up global state after each test."""
        players.clear()
        players_alive.clear()

    def test_player_count(self):
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

    def test_update_players_alive(self):
        players[0].alive = False
        update_players_alive(players)
        self.assertEqual(len(players_alive), 7)
        self.assertNotIn(players[0], players_alive)
        for player in players_alive:
            self.assertTrue(player.alive)

    def test_count_roles(self):
        mafia, townsfolk = count_roles(players_alive)
        self.assertEqual(mafia, 2)
        self.assertEqual(townsfolk, 6)
        for player in players_alive:
            if player.role == Role.MAFIA:
                player.alive = False
                break
        update_players_alive(players)
        mafia, townsfolk = count_roles(players_alive)
        self.assertEqual(mafia, 1)
        self.assertEqual(townsfolk, 6)

    def test_win_check_mafia_win(self):
        players_alive.clear()
        players_alive.extend([
            Player("P1", Role.MAFIA, alive=True),
            Player("P2", Role.MAFIA, alive=True),
            Player("P3", Role.TOWN, alive=True),
            Player("P4", Role.TOWN, alive=True)
        ])
        mafia, townsfolk = count_roles(players_alive)
        self.assertTrue(win_check(mafia, townsfolk))

    def test_win_check_townsfolk_win(self):
        players_alive.clear()
        players_alive.extend([
            Player("P1", Role.TOWN, alive=True),
            Player("P2", Role.TOWN, alive=True),
            Player("P3", Role.TOWN, alive=True),
            Player("P4", Role.TOWN, alive=True)
        ])
        mafia, townsfolk = count_roles(players_alive)
        self.assertTrue(win_check(mafia, townsfolk))

    def test_win_check_continue(self):
        players_alive.clear()
        players_alive.extend([
            Player("P1", Role.MAFIA, alive=True),
            Player("P2", Role.TOWN, alive=True),
            Player("P3", Role.TOWN, alive=True),
            Player("P4", Role.TOWN, alive=True),
            Player("P5", Role.TOWN, alive=True)
        ])
        mafia, townsfolk = count_roles(players_alive)
        self.assertFalse(win_check(mafia, townsfolk))

    def test_determine_winner(self):
        self.assertEqual(determine_winner(0), "Townsfolk")
        self.assertEqual(determine_winner(1), "Mafia")
        self.assertEqual(determine_winner(2), "Mafia")

    def test_night_vote_targets_townsfolk(self):
        target = night_vote(players_alive)
        self.assertIsNotNone(target)
        self.assertEqual(target.role, Role.TOWN)
        # Removed: self.assertFalse(target.alive)  # Handled in game_cycle

    def test_night_vote_no_townsfolk(self):
        players_alive.clear()
        players_alive.extend([
            Player("P1", Role.MAFIA, alive=True),
            Player("P2", Role.MAFIA, alive=True)
        ])
        target = night_vote(players_alive)
        self.assertIsNone(target)

    def test_day_vote_returns_player(self):
        day_killed = day_vote(players_alive)
        self.assertIsInstance(day_killed, Player)
        # Removed: self.assertFalse(day_killed.alive)  # Handled in game_cycle
        self.assertIn(day_killed.name, [p.name for p in players_alive])

    def test_day_vote_tie_breaking(self):
        results = []
        for _ in range(20):
            players_alive_copy = players_alive.copy()
            random.seed()  # Reset seed
            day_killed = day_vote(players_alive_copy)
            results.append(day_killed.name)
        unique_results = set(results)
        self.assertGreater(len(unique_results), 1)  # Ensure some variety

    def test_town_vote_excludes_self(self):
        voter = players_alive[0]
        for _ in range(10):
            vote = town_vote(voter, players_alive)
            self.assertIsNotNone(vote)
            self.assertNotEqual(vote, voter)

    def test_mafia_vote_excludes_mafia(self):
        voter = next(p for p in players_alive if p.role == Role.MAFIA)
        for _ in range(10):
            vote = mafia_vote(voter, players_alive)
            self.assertIsNotNone(vote)
            self.assertNotEqual(vote.role, Role.MAFIA)

    def test_ai_vote_no_valid_choices(self):
        voter_list = [Player("P1", Role.MAFIA, alive=True)]
        with self.assertRaises(ValueError):
            ai_vote(voter_list, exclude_voter=voter_list[0])

    def test_day_discuss_mafia_accuses_townsfolk(self):
        with captured_output() as output:
            day_discuss(players_alive, 1)
        output_text = output.getvalue()
        town_names = []
        for p in players_alive:
            if p.role == Role.TOWN:
                town_names.append(p.name)
        for player in players_alive:
            if player.role == Role.MAFIA:
                accusation = f"{player.name} accuses"
                self.assertIn(accusation, output_text)
                lines = output_text.split('\n')
                for line in lines:
                    if accusation in line:
                        accused_name = line.split("accuses ")[1].strip()
                        self.assertIn(accused_name, town_names)

    def test_game_cycle_terminates(self):
        players_alive.clear()
        players_alive.extend([
            Player("P1", Role.MAFIA, alive=True),
            Player("P2", Role.TOWN, alive=True)
        ])
        game_cycle()  # Should terminate quickly
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()