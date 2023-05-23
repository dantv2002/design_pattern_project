class Command:
    def execute(self):
        pass

class NormalAtackCommand(Command):
    def __init__(self,character,monster) -> None:
        self.monster = monster
        self.character = character

    def execute(self):
        self.monster.set_max_health(self.monster.get_max_health() - self.character.getAtk())
        self.monster.monster_atk(self.character)

class SkillUseCommand(Command):
    def __init__(self,character,monster) -> None:
        self.monster = monster
        self.character = character

    def execute(self):
        self.character.getSkill().use(self.character,self.monster)

class InputHandler:
    def __init__(self):
        pass

    def handle_input(self,command):
        command.execute()