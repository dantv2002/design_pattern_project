from MonsterAbstractFactory import MonsterAbstractFactory
from Level2Monster import Level2Monster

class Level2MonsterFactory(MonsterAbstractFactory):
    def create_monster(self, name):
        return Level2Monster(name)