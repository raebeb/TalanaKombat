from players import Player

from utils import check_who_has_the_first_turn, get_message_and_energy_to_discount

import json
import time

MAX_TURNS = 5

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
while first_player.is_alive and second_player.is_alive and turn < MAX_TURNS:
    time.sleep(1)
    first_player_movement = first_player.movements[turn]
    first_player_hit = first_player.hits[turn]
    energy_to_discount = get_message_and_energy_to_discount(first_player.name, first_player_movement, first_player_hit)

    if player2.energy > 0 and player2.energy - energy_to_discount > 0:
        player2.energy = player2.energy - energy_to_discount
    else:
        print(f"HA GANADO {player1.name} y aun le quedaban {player1.energy} puntos de energia!")
        player2.is_alive = False

    #### END PLAYER1'S TURN ###

    second_player_movement = second_player.movements[turn]
    second_player_hit = second_player.hits[turn]
    energy_to_discount = get_message_and_energy_to_discount(second_player.name, second_player_movement, second_player_hit)

    if player1.energy > 0 and player1.energy - energy_to_discount > 0:
        player1.energy = player1.energy - energy_to_discount
    else:
        print(f"HA GANADO {player2.name} y aun le quedaban {player2.energy} puntos de energia!")
        player1.is_alive = False

    ### END PLAYER2'S TURN ###

    turn += 1
