from GameLevel_Component import GameLevel_Component
from MonsterFactory import MonsterFactory

levels = ['','Easy', 'Normal', 'Hard']
class GameLevel_Leaf(GameLevel_Component):
    def __init__(self, name, level):
        monster_factory = MonsterFactory.get_factory(levels[level])
        self.__monster = monster_factory.create_monster(name)
    
    def get_name(self):
        return self.__monster.name
    
    def get_level(self):
        return self.__monster.level
    
    def get_max_health(self):
        return self.__monster.max_health
    
    def get_coin(self):
        return self.__monster.coin
    
    def set_max_health(self, current_health):
        self.__monster.max_health = current_health
    
    def set_coin(self, current_coin):
        self.__monster.coin = current_coin

    def monster_atk(self,character,reduce=0):
        self.__monster.normalAtk(character,reduce)