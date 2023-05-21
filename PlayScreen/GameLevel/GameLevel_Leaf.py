from GameLevel_Component import GameLevel_Component
from MonsterFactory import MonsterFactory

levels = ['','Easy', 'Normal', 'Hard']
class GameLevel_Leaf(GameLevel_Component):
    def __init__(self, name, level):
        _monster_factory = MonsterFactory.get_factory(levels[level])
        self._monster = _monster_factory.create_monster(name)
    
    def get_name(self):
        return self._monster.name
    
    def get_level(self):
        return self._monster.level
    
    def get_max_health(self):
        return self._monster.max_health
    
    def get_coin(self):
        return self._monster.coin
    
    def set_max_health(self, current_health):
        if self._monster.max_health > current_health and current_health >= 0:
            self._monster.max_health = current_health
    
    def set_coin(self, current_coin):
        if self._monster.coin > current_coin and current_coin >=0:
            self._monster.coin = current_coin