from abc import ABC, abstractmethod

class GameLevel_Component(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_level(self):
        pass

    @abstractmethod
    def get_max_health(self):
        pass

    @abstractmethod
    def get_coin(self):
        pass
    