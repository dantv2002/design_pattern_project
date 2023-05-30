class Character:
    
    def __init__(self, name, thisClass):
        self.name = name
        self.thisClass = thisClass
        self.skill = thisClass.getSkill()
        self.hp = thisClass.getHp()
        self.atk = thisClass.getAtk()
        self.gold = 0
        self.state = NormalState()

    #getter

    def getName(self):
        return self.name
    def getClass(self):
        return self.thisClass
    def getSkill(self):
        return self.skill
    def getGold(self):
        return self.gold
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

    def earnGold(self, gold):
        self.gold = self.gold + gold

    def save_state(self):
        return Memento(self.hp, self.atk)

    def restore_state(self, memento):
        self.hp = memento.hp
        self.atk = memento.atk

    def upgrade(self):
        self.state.upgrade(self)

    def set_state(self, state):
        self.state = state

class Memento:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk


class Caretaker:
    def __init__(self):
        self.mementos = []

    def save_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self):
        return self.mementos.pop()

class State:
    def upgrade(self, character):
        pass

class NormalState(State):
    def upgrade(self, character):
        # Tăng 10%
        character.atk = int(character.atk * 1.1)
        character.hp = int(character.hp * 1.1)   
        if (character.atk < 10):
            character.atk += 1
        elif (character.hp < 10):
            character.hp += 1

class StrongState(State):
    def upgrade(self, character):
         # Tăng 20%
        character.atk = int(character.atk * 1.2)
        character.hp = int(character.hp * 1.2)    
        if (character.atk < 10):
            character.atk += 1
        elif (character.hp < 10):
            character.hp += 1

