from Monster import Monster

class Level3Monster(Monster):
    def __init__(self,name):
        super().__init__(name, 3)
        self.health_factor = 1.5
        self.strength_factor = 1.5
        self.coin_factor = 1.5
        super().generate_random()
