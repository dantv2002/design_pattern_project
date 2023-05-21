from GameLevel_Component import GameLevel_Component

class GameLevel_Composite(GameLevel_Component):
    def __init__(self, name):
        self._name = name
        self._list_monster = []

    def add_monster(self, monster):
        self._list_monster.append(monster)

    def remove_monster(self, monster):
        self._list_monster.remove(monster)

    def get_name(self):
        return self._name

    @property
    def list_monster(self):
        return self._list_monster

    def get_level(self):
        total_level = 0
        for monster in self._list_monster:
            total_level += monster.get_level()
        return total_level


    def get_max_health(self):
        total_max_health = 0
        for monster in self._list_monster:
            total_max_health += monster.get_max_health()
        return total_max_health
    
    def get_coin(self):
        total_coin = 0
        for monster in self._list_monster:
            total_coin += monster.get_coin()
        return total_coin