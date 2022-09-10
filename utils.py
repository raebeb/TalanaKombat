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

def discount_energy_points(player1, player2):
    """_summary_

    Args:
        player1 (_type_): _description_
        player2 (_type_): _description_
    """
    #TODO: finish this method


def check_energy(player: Player) -> int:
    """
    method used at first of each turn to check if the player has enough energy to keep fighting

    Args:
        player (Player): Player object to check its energy

    Returns:
        int: Number of energy points left 
    """

    return player.energy

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
        # Taladoken
        if movement == "DSD" and hit == "P":
            print("Tonnyn Stallone usa un Taladoken!")
            return 3
        # Remuyuken
        if movement == "DS" and hit == "P":
            print("Tonnyn Stallone usa un Remuyuken!")
            return 2
        
        # no movement

        if movement == "" and hit != "":
            detail_hit = "una patada!" if hit == "K" else "un puñetazo!"
            print(f"Tonnyn Stallone da {detail_hit}")
            return 1

    else:
        # Taladoken
        if movement == "ASA" and hit == "P":
            print("Arnaldold Schuatseneger usa un Taladoken!")
            return 2
        # Remuyuken
        if movement == "SA" and hit == "K":
            print("Arnaldold Scchuatseneger usa un Remuyuken!")
            return 3
        
        # no movement

        if movement == "" and hit != "":
            detail_hit = "una patada!" if hit == "K" else "un puñetazo!"
            print(f"Arnaldold Scchuatseneger da {detail_hit}")
            return 1
        

