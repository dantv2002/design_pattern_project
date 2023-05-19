class HealSkill:
    type = "heal"

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getType(self):
        return self.type