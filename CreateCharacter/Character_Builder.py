import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from CreateCharacter.Character import Character

class CharacterBuilder:
    def __init__(self):
        self.name = None
        self.thisClass = None

    def set_name(self, name):
        self.name = name
    def set_class(self, thisClass):
        self.thisClass = thisClass

    def build(self):
        return Character(self.name, self.thisClass)