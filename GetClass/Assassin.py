import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from CreateSkill.Skill_Factory import SkillFactory

class Assassin:
    #attribute
    name = "Assassin"
    hp = 5
    atk = 20
    skill = None

    def __init__(self):
        factory = SkillFactory()
        self.skill = factory.create("dmg", "Double splash", 25, 2)
    
    #func
    def getHp(self):
        return self.hp
    
    def getAtk(self):
        return self.atk
    
    def getName(self):
        return self.name
    
    def getSkill(self):
        return self.skill