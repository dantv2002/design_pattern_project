from Monster import Monster

class Level2Monster(Monster):
    def __init__(self,name):
        super().__init__(name, 2)
        self.health_factor = 1
        self.strength_factor = 1
        self.coin_factor = 1
        super().generate_random()