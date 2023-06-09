import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

from TestMonster.TestMonster import TestMonster
from CreateCharacter.Character import Caretaker
from PlayScreen.Create_Play_Screen import Create_Play_Screen
from FightCommand.FightCommandPattern import InputHandler, NormalAtackCommand, SkillUseCommand

class Screen3(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Screen 3 - Play")
        self.counter = 0
        self.skillCD = 0
        self.skillCD = 0
        self.numberSkill = tk.StringVar()
        self.play_screen = None
        self.input_handler = None
        self.caretaker = None
        self.initial_state = None
        self.caretaker = None
        player_photo = ImageTk.PhotoImage(Image.open("player_image.png").resize((200, 200), Image.LANCZOS))
        self.labelPlayer = tk.Label(self, image=player_photo)
        self.labelPlayer.image = player_photo
        enemy_photo = ImageTk.PhotoImage(Image.open("enemy_image.png").resize((200, 200), Image.LANCZOS))
        self.labelEnemy = tk.Label(self, image=enemy_photo)
        self.labelEnemy.image = enemy_photo
        self.buttonSkill1 = tk.Button(self, text="Normal attack", command=lambda: self.set_number_skill("0"))
        self.buttonSkill2 = tk.Button(self, text="Skill 2", command=lambda: self.set_number_skill("1"))
        self.text_box = tk.Text(self)
        self.labelCharHP = tk.Label(self)
        self.labelMonsterHP = tk.Label(self)
        self.labelMonsterName = tk.Label(self)

        
    def set_number_skill(self, skill):
        self.numberSkill.set(skill)
            
    def startARound(self):
        self.reset()
        self.play_screen = Create_Play_Screen(play_screen_level=int(self.master.levelInput)).create()
        self.input_handler = InputHandler()
        self.caretaker = Caretaker()
        self.initial_state = self.master.myCharacters.save_state()
        self.caretaker.save_memento(self.initial_state)
        self.text_box.delete("1.0", tk.END)
        #Start the game
        while self.counter < self.play_screen.list_monster.__len__() and self.master.myCharacters.getHp() > 0: #This first While loop will break if all the monster are down or the character HP are below 0
            self.text_box.see(tk.END)
            self.text_box.insert(tk.END, "You will face the: " + self.play_screen.list_monster[self.counter].get_name() + "\n")
            self.labelMonsterName.config(text=self.play_screen.list_monster[self.counter].get_name())
            while self.play_screen.list_monster[self.counter].get_max_health() > 0 and self.master.myCharacters.getHp() > 0:#This while loop will be the main game play for each monster     
                self.wait_variable(self.numberSkill)
                numberSkill = self.numberSkill.get()
                self.labelCharHP.config(text=self.master.myCharacters.getHp())
                self.labelMonsterHP.config(text=self.play_screen.list_monster[self.counter].get_max_health())
                if(numberSkill == "0"):
                    self.input_handler.handle_input(NormalAtackCommand(self.master.myCharacters,self.play_screen.list_monster[self.counter]))
                    if(self.skillCD > 0):
                        self.skillCD = self.skillCD - 1
                    self.text_box.insert(tk.END, "Character HP " + str(self.master.myCharacters.getHp()) + "\n")
                    self.text_box.insert(tk.END, "Monster HP " + str(self.play_screen.list_monster[self.counter].get_max_health()) + "\n")
                    self.text_box.insert(tk.END, "Normal attack" + "\n")
                    self.labelCharHP.config(text=self.master.myCharacters.getHp())
                    self.labelMonsterHP.config(text=self.play_screen.list_monster[self.counter].get_max_health())
                    self.buttonSkill2.config(text="Skill 2: CD " + str(self.skillCD) +" step")
                    self.text_box.see(tk.END)
                elif(numberSkill == "1"):
            
                    if(self.skillCD == 0):
                        self.input_handler.handle_input(SkillUseCommand(self.master.myCharacters,self.play_screen.list_monster[self.counter]))
                        self.skillCD = self.master.myCharacters.getSkill().getCoolDown()
                        self.text_box.insert(tk.END, "Character HP " + str(self.master.myCharacters.getHp()) + "\n")
                        self.text_box.insert(tk.END, "Monster HP " + str(self.play_screen.list_monster[self.counter].get_max_health()) + "\n")
                        self.labelCharHP.config(text=self.master.myCharacters.getHp())
                        self.labelMonsterHP.config(text=self.play_screen.list_monster[self.counter].get_max_health())
                    else: 
                        self.text_box.insert(tk.END, "Skill 2 Cooldown " + str(self.skillCD) + "\n")
                    self.text_box.see(tk.END)
                    self.buttonSkill2.config(text="Skill 2: CD " + str(self.skillCD) +" step")
            if(self.master.myCharacters.getHp() > 0):
                self.text_box.insert(tk.END, "Next Monster is comming " + "\n")
                self.master.myCharacters.earnGold(self.play_screen.list_monster[self.counter].get_coin())
                self.text_box.delete("1.0", tk.END)
                self.counter = self.counter + 1
                self.text_box.see(tk.END)                    
                self.buttonSkill1.config(text="Normal attack")
                self.buttonSkill2.config(text="Skill 2")


        if self.master.myCharacters.getHp() > 0:
            self.show_game_finish_message("You win!!!")
        else:
            self.show_game_finish_message("You Lose !!!")
        
        memento = self.caretaker.get_memento()
        self.master.myCharacters.restore_state(memento)
        self.master.show_screen2()
        
    def show_game_finish_message(self, message):
            message_box = messagebox.showinfo("Game finish!", message)
            self.focus_force()
            
    def reset(self):
        self.master.levelInput = 1
        self.counter = 0
        self.skillCD = 0
        self.skillCD = 0
        self.numberSkill = tk.StringVar()
        self.play_screen = None
        self.input_handler = None
        self.caretaker = None
        self.initial_state = None
        self.caretaker = None
    
    def show(self):
        self.buttonSkill1.place(x=100, y=500, width=120, height=40)
        self.buttonSkill2.place(x=250, y=500, width=120, height=40)
        self.text_box.place(x=400, y=500, width=300, height=80)
        self.labelPlayer.place(x=100, y=200, width=200, height=200)
        self.labelEnemy.place(x=500, y=200, width=200, height=200)
        self.labelCharHP.place(x=100, y=160, width=200, height=40)
        self.labelMonsterHP.place(x=500, y=160, width=200, height=40)
        self.labelMonsterName.place(x=500, y=120, width=200, height=40)
        self.deiconify()

    def hide(self):
        self.withdraw()

