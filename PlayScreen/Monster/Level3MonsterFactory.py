from MonsterAbstractFactory import MonsterAbstractFactory
from Level3Monster import Level3Monster

class Level3MonsterFactory(MonsterAbstractFactory):
    def create_monster(self, name):
        return Level3Monster(name)
