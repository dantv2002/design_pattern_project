from Monster import Monster

class Level1Monster(Monster):
    def __init__(self, name):
        super().__init__(name, 1)
        self.health_factor = 0.5
        self.strength_factor = 0.5
        self.coin_factor = 0.5
        super().generate_random()
