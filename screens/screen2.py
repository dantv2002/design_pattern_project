import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

class Screen2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Screen 2 - Thông tin nhân vật")
        self.GoldForUpgrade = 0
        self.levelInput = tk.StringVar(value="1")
        self.comboLevel = ttk.Combobox(self, textvariable=self.levelInput, values=[str(i) for i in range(1, 11)])
        self.labelCharName = tk.Label(self, text="Tên: ")
        self.labelClassName = tk.Label(self, text="Lớp: ")
        self.labelHp = tk.Label(self, text="HP: ")
        self.labelSkill = tk.Label(self, text="Skill: ")
        self.labelAtk = tk.Label(self, text="ATK: ")
        self.labelGold = tk.Label(self, text="Gold: ")
        self.labelGoldForUpgrade = tk.Label(self, text="Gold cần để nâng cấp: ")
        self.labelInputLevel = tk.Label(self, text = "Chọn Level: ")
        self.buttonTaoNhanVat = tk.Button(self, text="Tạo lại nhân vật", command=self.master.show_screen1)
        self.buttonBatDauGame = tk.Button(self, text="Bắt đầu game", command=self.startGame)
        self.buttonUpgrade = tk.Button(self, text="Nâng cấp", command=self.upgrade)
        if self.master.myCharacters is None:
            self.labelCharName.config(text="Chưa tạo nhân vật")
        else:
            # self.master.myCharacters.setGold(100)
            self.labelCharName.config(text="Tên: " + self.master.myCharacters.getName())
            self.labelClassName.config(text="Lớp: " + self.master.myCharacters.getClass().getName())
            self.labelHp.config(text="HP: " + str(self.master.myCharacters.getHp()))
            self.labelSkill.config(text="Skill: " + self.master.myCharacters.getSkill().getName())
            self.labelAtk.config(text="ATK: " + str(self.master.myCharacters.getAtk()))
            self.labelGold.config(text="Gold: " + str(self.master.myCharacters.getGold()))
            self.GoldForUpgrade = int((self.master.myCharacters.getHp() + self.master.myCharacters.getAtk()) / 5)
            self.labelGoldForUpgrade.config(text="Gold cần để nâng cấp: " + str(self.GoldForUpgrade))
    
    def startGame(self):
        self.master.show_screen3()
        self.master.screen3.startARound()
            
    def upgrade(self):
        if(self.GoldForUpgrade < self.master.myCharacters.getGold()):
            self.master.myCharacters.upgrade()
            self.master.myCharacters.setGold(self.master.myCharacters.getGold() - self.GoldForUpgrade)
            self.labelCharName.config(text="Tên: " + self.master.myCharacters.getName())
            self.labelClassName.config(text="Lớp: " + self.master.myCharacters.getClass().getName())
            self.labelHp.config(text="HP: " + str(self.master.myCharacters.getHp()))
            self.labelSkill.config(text="Skill: " + self.master.myCharacters.getSkill().getName())
            self.labelAtk.config(text="ATK: " + str(self.master.myCharacters.getAtk()))
            self.labelGold.config(text="Gold: {:.1f}".format(self.master.myCharacters.getGold()))
            self.GoldForUpgrade = (self.master.myCharacters.getHp() + self.master.myCharacters.getAtk()) / 5
            self.labelGoldForUpgrade.config(text="Gold cần để nâng cấp: {:.1f}".format(self.GoldForUpgrade))
        else:
            messagebox.showerror("Lỗi nâng cấp", "Không đủ gold")
        
    def show(self):
        self.labelCharName.place(x = 50, y = 50, height=50, width=100)
        self.labelClassName.place(x = 50, y = 100, height=50, width=100)
        self.labelHp.place(x = 50, y = 150, height=50, width=100)
        self.labelSkill.place(x = 50, y = 200, height=50, width=100)
        self.labelAtk.place(x = 50, y = 250, height=50, width=100)
        self.labelGold.place(x = 50, y = 300, height=50, width=100)
        self.buttonTaoNhanVat.place(x = 50, y = 450, height=60, width=100)
        self.buttonBatDauGame.place(x = 450, y = 250, height=100, width=200)
        self.buttonBatDauGame.configure(bg="cyan")
        self.buttonUpgrade.place(x = 250, y = 350, height=60, width=100)
        self.labelGoldForUpgrade.place(x = 50, y = 350, height=60, width=200)
        self.comboLevel.place(x= 650, y=170, width=100, height=40)
        self.labelInputLevel.place(x= 430, y=170, width=100, height=40)
        self.deiconify()

    def hide(self):
        self.withdraw()
