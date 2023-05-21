# abstract factory
from abc import ABC, abstractmethod

class MonsterAbstractFactory(ABC):
    @abstractmethod
    def create_monster(self, name):
        pass