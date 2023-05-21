from MonsterAbstractFactory import MonsterAbstractFactory
from Level1Monster import Level1Monster

class Level1MonsterFactory(MonsterAbstractFactory):
    def create_monster(self, name):
        return Level1Monster(name)