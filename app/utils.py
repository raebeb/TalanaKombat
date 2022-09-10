from players import Player

def check_who_has_the_first_turn(player1: Player, player2: Player) -> Player:
    """
    Method used to check wich player has the first turn of the figth

    Args:
        player1 (Player): player who appears first in the json file
        player2 (Player): player who appears last in the json file

    Returns:
        Player: the player who has the first turn of the figth
    """
    # check number of movements
    if len(player1.movements) != len(player2.movements):
        first_turn = player1 if len(player1.movements) < len(player2.movements) else player2
        return first_turn

    # check number of hits
    if len(player1.hits) != len(player2.hits):
        first_turn = player1 if len(player1.hits) < len(player2.hits) else player2
        return first_turn

    # if none of above 
    return player1

def get_message_and_energy_to_discount(player_name: str, movement: str, hit: str) -> int:
    """
    Method used to determine the message to show in console and know how many damage was done

    Args:
        name (str): Name of the player
        movement (str): Combinations of buttons 
        hit (str): a character representing the hit 

    Returns:
        int: Number of energy points to discount to the other player
    """

    if player_name == "Tonnyn Stallone":
        movements_dict = {
                "A": "Tonnyn Stallone retrocede",
                "S": "Tonnyn Stallone se agacha",
                "D": "Tonnyn Stallone avanza",
                "W": "Tonnyn Stallone salta"
            }

        # Taladoken
        if movement == "DSD" and hit == "P":
            print("Tonnyn Stallone usa un Taladoken!")
            return 3

        # Remuyuken
        if movement == "DS" and hit == "K":
            print("Tonnyn Stallone usa un Remuyuken!")
            return 2
        
        # only hit, no movement 
        if movement == "" and hit != "":
            detail_hit = "una patada!" if hit == "K" else "un puñetazo!"
            print(f"Tonnyn Stallone da {detail_hit}")
            return 1

        #only movement, no hit
        if movement != "" and hit == "":
            # if only on button is used
            if len(movement) == 1:
                print(movements_dict[movement])
                return 0
            else:
                print("Tonnyn stallone se mueve")
                return 0
        
        # movement and hit, but no special
        if movement != "" and hit != "":
            hit_message = "y da una patada" if hit == "K" else "y da un puñetazo"
            if len(movement) == 1:
                print(f"{movements_dict[movement]} {hit_message}")
                return 1
            else:
                print(f"Tonnyn Stallone se mueve {hit_message}")
                return 1

    else:
        movements_dict = {
                "A": "Arnaldold Schuatseneger avanza",
                "S": "Arnaldold Schuatseneger se agacha",
                "D": "Arnaldold Schuatseneger retrocede",
                "W": "Arnaldold Schuatseneger salta"
            }

        # Taladoken
        if movement == "ASA" and hit == "P":
            print("Arnaldold Schuatseneger usa un Taladoken!")
            return 2

        # Remuyuken
        if movement == "SA" and hit == "K":
            print("Arnaldold Scchuatseneger usa un Remuyuken!")
            return 3
        
        # only hit, no movement
        if movement == "" and hit != "":
            detail_hit = "una patada!" if hit == "K" else "un puñetazo!"
            print(f"Arnaldold Scchuatseneger da {detail_hit}")
            return 1

        #only movement, no hit
        if movement != "" and hit == "":
            # if only on button is used
            if len(movement) == 1:
                print(movements_dict[movement])
                return 0
            else:
                print("Arnaldold Schuatseneger se mueve")
                return 0    

        # movement and hit, but no special
        if movement != "" and hit != "":
            hit_message = "y da una patada" if hit == "K" else "y da un puñetazo"
            if len(movement) == 1:
                print(f"{movements_dict[movement]} {hit_message}")
                return 1
            else:
                print(f"Arnaldold Schuatseneger se mueve {hit_message}")
                return 1
