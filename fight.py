from players import Player

from utils import check_who_has_the_first_turn, get_message_and_energy_to_discount

import json


input_file = open("input.json")
data = json.load(input_file)

# Create objects for each player
players = list(data.keys())

name1 = players[0]
movements1 = data["player1"]["movimientos"]
hits1 = data["player1"]["golpes"]
player1 = Player(name1, movements1, hits1)

name2 = players[1]
movements2 = data["player2"]["movimientos"]
hits2 = data["player2"]["golpes"]
player2 = Player(name2, movements2, hits2)


#Define who starts the fight
first_player = check_who_has_the_first_turn(player1, player2)
second_player = player1 if first_player != player1 else player2

# Start Fight!

turn = 0
while first_player.is_alive and second_player.is_alive and turn < 5:
    first_player_movement = first_player.movements[turn]
    first_player_hit = first_player.hits[turn]
    energy_to_discount = get_message_and_energy_to_discount(first_player.name, first_player_movement, first_player_hit)
    print(f"ENERGY TO Disc {energy_to_discount}")
    turn += 1










