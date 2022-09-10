import sys
sys.path.append("..")

import unittest
import repackage
repackage.up()

from utils import check_who_has_the_first_turn, get_message_and_energy_to_discount
from players import Player

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("player1", [], [])
        self.player2 = Player("player2", [], [])

    def test_player1_has_the_first_turn(self):
        self.player1.movements = ["A", "A", "A"]
        self.player2.movements = ["A", "A", "A", "A"]
        self.assertEqual(check_who_has_the_first_turn(self.player1, self.player2), self.player1)

    def test_player2_has_the_first_turn(self):
        self.player1.movements = ["A", "A", "A", "A"]
        self.player2.movements = ["A", "A", "A"]
        self.assertEqual(check_who_has_the_first_turn(self.player1, self.player2), self.player2)

    def test_player1_taladoken(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "DSD", "P"), 3)

    def test_player1_remuyuken(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "DS", "K"), 2)

    def test_player1_kick(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "", "K"), 1)

    def test_player1_punch(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "", "P"), 1)

    def test_player1_one_movement_no_hit(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "A", ""), 0)
    
    def test_player1_multiple_movement_no_hit(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "ASD", ""), 0)

    def test_player1_one_movement_and_hit_no_special(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "A", "P"), 1)

    def test_player1_multiple_movement_and_hit_no_special(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player1.name, "ASD", "P"), 1)



    def test_player2_taladoken(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "ASA", "P"), 2)

    def test_player2_remuyuken(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "SA", "K"), 3)

    def test_player2_kick(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "", "K"), 1)

    def test_player2_punch(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "", "P"), 1)

    def test_player2_one_movement_no_hit(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "A", ""), 0)
    
    def test_player2_multiple_movement_no_hit(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "ASD", ""), 0)

    def test_player2_one_movement_and_hit_no_special(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "A", "P"), 1)

    def test_player2_multiple_movement_and_hit_no_special(self):
        self.assertEqual(get_message_and_energy_to_discount(self.player2.name, "ASD", "P"), 1)

    def tearDown(self) -> None:
        return super().tearDown()
