
class Player():
    def __init__(self, name, movements, hits):
        self.name = "Tonnyn Stallone" if name == "player1" else "Arnaldold Schuatseneger"
        self.movements = movements
        self.hits = hits
        self.energy = 6
        self.is_alive = True

    
