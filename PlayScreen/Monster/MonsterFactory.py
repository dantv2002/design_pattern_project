from Level1MonsterFactory import Level1MonsterFactory
from Level2MonsterFactory import Level2MonsterFactory
from Level3MonsterFactory import Level3MonsterFactory

class MonsterFactory():
    @staticmethod
    def get_factory(level):
        if level == 'Easy':
            return Level1MonsterFactory()
        elif level == 'Normal':
            return Level2MonsterFactory()
        elif level == 'Hard':
            return Level3MonsterFactory()
        else:
            raise ValueError(f'Unsupported monster level: {level}')