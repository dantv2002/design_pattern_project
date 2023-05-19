class Character:
    
    def __init__(self, name, thisClass, skill):
        self.name = name
        self.thisClass = thisClass
        self.skill = skill
        self.hp = thisClass.getHp()
        self.atk = thisClass.getAtk()
        self.gold = 0


    #getter

    def getName(self):
        return self.name
    def getClass(self):
        return self.thisClass
    def getSkill(self):
        return self.skill
    def getGold(self):
        return self.gold
    def getClass(self):
        return self.thisClass
    def getHp(self):
        return self.hp
    def getAtk(self):
        return self.atk
    
    
    #setter
    def setGold(self, gold):
        self.gold = gold
    def setHp(self, hp):
        self.hp = hp
    def setAtk(self, atk):
        self.atk = atk

    