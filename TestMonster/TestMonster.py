class TestMonster:

    def __init__(self,name,hp,atk,gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.gold = gold


    def getName(self):
        return self.name
    def getHp(self):
        return self.hp
    def getAtk(self):
        return self.atk
    def getGold(self):
        return self.gold
    
    def setHp(self,hp):
        self.hp = hp

    def normalAtk(self,character):
        character.setHp(character.getHp() - self.atk)