import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from CreateSkill import Dmg_Skill, Heal_Skill, Reduce_Skill

class SkillFactory:
    @staticmethod
    def create(type, name, power, cd):
        if type == "dmg":
            return Dmg_Skill.DmgSkill(name, power, cd)
        elif type == "heal":
            return Heal_Skill.HealSkill(name, power, cd)
        elif type == "reduce":
            return Reduce_Skill.ReduceSkill(name, power, cd)
        else:
            raise ValueError("Invalid type!")