import tkinter as tk

class Screen1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Screen 1 - Tạo nhân vật")
        self.classVar = tk.IntVar()
        self.nameVar = tk.StringVar()
        
        self.labelName = tk.Label(self, text="Tên của bạn là: ")
        self.entryName = tk.Entry(self, textvariable=self.nameVar)
        self.labelClass = tk.Label(self, text="Class của bạn là: ")
        self.radiobtn0 = tk.Radiobutton(self, text="Mage", variable=self.classVar, value=0)
        self.radiobtn1 = tk.Radiobutton(self, text="Warrior", variable=self.classVar, value=1)
        self.radiobtn2 = tk.Radiobutton(self, text="Assassin", variable=self.classVar, value=2)
        self.radiobtn3 = tk.Radiobutton(self, text="Priest", variable=self.classVar, value=3)
        self.createCharBtn = tk.Button(self, text="Create character", command=self.createCharBtn_click )
        if self.master.myCharacters is None:
            self.nameVar.set("name1")
        else:
            self.nameVar.set(self.master.myCharacters.getName())
            self.entryName.config(textvariable=self.nameVar, text = self.nameVar.get())
    
    def createCharBtn_click(self):
        if self.master.myCharacters is None:
            self.nameVar.set(self.entryName.get())
            self.master.create_Character(self.entryName.get(), self.classVar.get())
            # print(self.nameVar.get())
        else:
            self.nameVar.set(self.master.myCharacters.getName())
            self.entryName.config(textvariable=self.nameVar, text = self.nameVar.get())
            self.nameVar.set(self.entryName.get())
            self.master.create_Character(self.entryName.get(), self.classVar.get())
            # print(self.nameVar.get())
        self.master.show_screen2()
    
    def show(self):
        self.labelName.place(x = 50, y = 50, height=50, width=100)
        self.entryName.place(x = 50, y = 200, height=50, width=100)
        self.labelClass.place(x = 350, y = 50, height=50, width=100)
        self.radiobtn0.place(x = 220, y = 200, height=50, width=100)
        self.radiobtn1.place(x = 370, y = 200, height=50, width=100)
        self.radiobtn2.place(x = 520, y = 200, height=50, width=100)
        self.radiobtn3.place(x = 670, y = 200, height=50, width=100)
        self.createCharBtn.place(x = 350, y = 350, height=60, width=100, bordermode="inside")
        self.createCharBtn.configure(bg="cyan")
        self.deiconify()

    def hide(self):
        self.withdraw()
        
