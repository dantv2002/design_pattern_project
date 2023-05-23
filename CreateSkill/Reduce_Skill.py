class ReduceSkill:
    type = "reduce"

    def __init__(self, name, power, cd):
        self.name = name
        self.power = power
        self.cd = cd

    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getType(self):
        return self.type
    def getCoolDown(self):
        return self.cd
    
    def use(self,character,monster):
        monster.set_max_health(monster.get_max_health() - character.getAtk())
        monster.monster_atk(character,self.power)