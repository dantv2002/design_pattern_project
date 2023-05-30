import sys
import os
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_folder, ".."))

from CreateSkill.Skill_Factory import SkillFactory
from GetClass.ClassFactory import ClassFactory
from CreateCharacter.Character_Builder import CharacterBuilder
from TestMonster.TestMonster import TestMonster
from CreateCharacter.Character import Caretaker
from PlayScreen.Create_Play_Screen import Create_Play_Screen

from FightCommand.FightCommandPattern import InputHandler,NormalAtackCommand,SkillUseCommand

def main():
    skillFactory = SkillFactory()
    classFactory = ClassFactory()

    charBuilder = CharacterBuilder()
    charBuilder.set_name("ThoTy")
    charBuilder.set_class(classFactory.create("warrior")) #mage, warrior, assassin, priest

    myChar = charBuilder.build()
    print(f"name: {myChar.getName()}, gold: {myChar.getGold()}, skill: {myChar.getSkill().getName()}, class: {myChar.getClass().getName()}, hp: {myChar.getHp()}")
    myChar.upgrade()
    print(f"name: {myChar.getName()}, gold: {myChar.getGold()}, skill: {myChar.getSkill().getName()}, class: {myChar.getClass().getName()}, hp: {myChar.getHp()}")
    myChar.upgrade()
    print(f"name: {myChar.getName()}, gold: {myChar.getGold()}, skill: {myChar.getSkill().getName()}, class: {myChar.getClass().getName()}, hp: {myChar.getHp()}")
    myChar.upgrade()
    print(f"name: {myChar.getName()}, gold: {myChar.getGold()}, skill: {myChar.getSkill().getName()}, class: {myChar.getClass().getName()}, hp: {myChar.getHp()}")
    startARound(myChar)
    print("Real Gold: ",myChar.getGold())
    # print(f"name: {myChar.getName()}, gold: {myChar.getGold()}, skill: {myChar.getSkill().getName()}, class: {myChar.getClass().getName()}, hp: {myChar.getHp()}")


def startARound(myChar):
    # Create Gamescreen
    print("Choose The Level: ")
    levelInput = input()
    create_play_screen = Create_Play_Screen(play_screen_level=int(levelInput))
    play_screen = create_play_screen.create()
    #Create Character status to prepare for attack
    counter = 0 # Count the number of monster
    skillCD = 0 # Skill Cooldown for skill use
    #Memento to save the start stark of the character
    input_handler = InputHandler()
    caretaker = Caretaker()
    initial_state = myChar.save_state()
    caretaker.save_memento(initial_state)

    #Start the game
    while counter < play_screen.list_monster.__len__() and myChar.getHp() > 0: #This first While loop will break if all the monster are down or the character HP are below 0
        print("You will face the: ",play_screen.list_monster[counter].get_name())
        while play_screen.list_monster[counter].get_max_health() > 0 and myChar.getHp() > 0:#This while loop will be the main game play for each monster     
            print("Choose Your Atk: ")
            numberSkill = input()
            if(numberSkill == "0"):
                input_handler.handle_input(NormalAtackCommand(myChar,play_screen.list_monster[counter]))
                if(skillCD > 0):
                    skillCD = skillCD - 1
                print("Character HP",myChar.getHp())
                print("Monster HP",play_screen.list_monster[counter].get_max_health())
                print("Skill Cooldown", skillCD)
            elif(numberSkill == "1"):
                if(skillCD == 0):
                    input_handler.handle_input(SkillUseCommand(myChar,play_screen.list_monster[counter]))
                    skillCD = myChar.getSkill().getCoolDown()
                    
                    print("Character HP",myChar.getHp())
                    print("Monster HP",play_screen.list_monster[counter].get_max_health())
                else: print("Your skill is on Cooldown")
        if(myChar.getHp() > 0):
            print("Next Monster is comming")
            myChar.earnGold(play_screen.list_monster[counter].get_coin())
            counter = counter + 1

    #finish pla
    if(myChar.getHp() > 0):
        print("You Win !!!")
    else:
        print("You Lose !!!")

    memento = caretaker.get_memento()
    myChar.restore_state(memento)


main()