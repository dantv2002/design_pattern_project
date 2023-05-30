from abc import ABC, abstractmethod
import random

class Monster(ABC):
    @abstractmethod
    def __init__(self, name, level):
        self.__name = name
        self.__level = level
        self.__max_health = 0
        self.__strength = 0
        self.__coin = 0
    def generate_random(self):
        self.__max_health = round(random.uniform(40, 70) * self.__level * self.health_factor)
        self.__strength = round(random.uniform(1, 5) * self.__level * self.strength_factor)
        self.__coin = round(random.uniform(10, 30) * self.__level * self.coin_factor)

    # getter/setter
    @property
    def name(self):
        return self.__name
    
    @property
    def level(self):
        return self.__level
    
    @property
    def max_health(self):
        return self.__max_health
    
    @property
    def strength(self):
        return self.__strength
    
    @property
    def coin(self):
        return self.__coin
    
    @max_health.setter
    def max_health(self, current_health):
        if self.__max_health > current_health:
            self.__max_health = current_health
    
    @coin.setter
    def coin(self, current_coin):
        if self.__coin > current_coin and current_coin >=0:
            self.__coin = current_coin

    def normalAtk(self,character,reduce=0):
        monsterDame = (self.__strength - reduce) if (self.__strength - reduce) > 0 else 0
        print("monster Dame: ", monsterDame)
        character.setHp(character.getHp() - monsterDame)
    

