import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from CreateSkill.Skill_Factory import SkillFactory
from GetClass.ClassFactory import ClassFactory
from CreateCharacter.Character_Builder import CharacterBuilder

def main():
    skillFactory = SkillFactory()
    classFactory = ClassFactory()

    charBuilder = CharacterBuilder()
    charBuilder.set_name("ThoTy")
    charBuilder.set_class(classFactory.create("priest")) #mage, warrior, assassin, priest

    myChar = charBuilder.build()

    print(f"name: {myChar.getName()}, gold: {myChar.getGold()}, skill: {myChar.getSkill().getName()} with power {myChar.getSkill().getPower()}, class: {myChar.getClass().getName()}, hp: {myChar.getHp()}")

main()