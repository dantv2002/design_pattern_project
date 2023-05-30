import tkinter as tk
from tkinter import messagebox

from screens.screen1 import Screen1
from screens.screen2 import Screen2
from screens.screen3 import Screen3
from CreateSkill.Skill_Factory import SkillFactory
from GetClass.ClassFactory import ClassFactory
from CreateCharacter.Character_Builder import CharacterBuilder


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Game")
        self.myCharacters = None
        self.levelInput = None
        self.screen1 = Screen1(self)
        self.screen2 = Screen2(self)
        self.screen3 = Screen3(self)
        self.show_screen1()

    def show_screen1(self):
        self.withdraw()
        self.hide_all()
        self.center_window(self.screen1)
        self.screen1.show()

    def show_screen2(self):
        self.hide_all()
        self.center_window(self.screen2)
        self.screen2.show()

    def show_screen3(self):
        self.hide_all()
        self.center_window(self.screen3)
        self.screen3.show()

    def hide_all(self):
        self.screen1.destroy()
        self.screen2.destroy()
        self.screen3.destroy()
        self.screen1 = Screen1(self)
        self.screen2 = Screen2(self)
        self.screen3 = Screen3(self)
        self.screen1.hide()
        self.screen2.hide()
        self.screen3.hide()

    def center_window(self, window):
        window.update_idletasks()
        width = 800
        height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_Character(self, name, charClass = 0):
        skillFactory = SkillFactory()
        classFactory = ClassFactory()

        charBuilder = CharacterBuilder()
        charBuilder.set_name(name)
        #mage = 0, warrior = 1, assassin = 2, priest = 3
        if charClass == 0:
            charBuilder.set_class(classFactory.create("mage"))
        elif charClass == 1: 
            charBuilder.set_class(classFactory.create("warrior"))
        elif charClass == 2: 
            charBuilder.set_class(classFactory.create("assassin"))
        else:
            charBuilder.set_class(classFactory.create("priest"))
        char = charBuilder.build()
        messagebox.showinfo("Tạo nhân vật", f"Tạo thành công với tên <{char.getName()}>, thuộc class <{char.getClass().getName()}>")
        self.myCharacters = char
        # print(self.myCharacters.getName()+self.myCharacters.getClass().getName())


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
