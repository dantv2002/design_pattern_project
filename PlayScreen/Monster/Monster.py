from abc import ABC, abstractmethod
import random

class Monster(ABC):
    @abstractmethod
    def __init__(self, name, level):
        self._name = name
        self._level = level
        self._max_health = 0
        self._strength = 0
        self._coin = 0
    def generate_random(self):
        self._max_health = round(random.uniform(5, 10) * self._level * self.health_factor)
        self._strength = round(random.uniform(1, 5) * self._level * self.strength_factor)
        self._coin = round(random.uniform(10, 15) * self._level * self.coin_factor)

    # getter/setter
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def max_health(self):
        return self._max_health
    
    @property
    def strength(self):
        return self._strength
    
    @property
    def coin(self):
        return self._coin
    
    @max_health.setter
    def max_health(self, current_health):
        self._max_health = current_health
    
    @coin.setter
    def coin(self, curren_coin):
        self._coin = curren_coin
    

