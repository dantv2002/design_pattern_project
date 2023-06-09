import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from GetClass import Assassin, Mage, Warrior, Priest

class ClassFactory:
    @staticmethod
    def create(role):
        if role == "mage":
            return Mage.Mage()
        elif role == "warrior":
            return Warrior.Warrior()
        elif role == "assassin":
            return Assassin.Assassin()
        elif role == "priest":
            return Priest.Priest()
        else:
            raise ValueError("Invalid class!")