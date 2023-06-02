import unittest
from MonsterFactory import MonsterFactory
from Level1MonsterFactory import Level1MonsterFactory
from Level2MonsterFactory import Level2MonsterFactory
from Level3MonsterFactory import Level3MonsterFactory

levels = ['Easy', 'Normal', 'Hard']
class TestMonsterFatory(unittest.TestCase):

    def test_get_factory(self):
        self.assertIsInstance(MonsterFactory.get_factory(levels[0]), Level1MonsterFactory)
        self.assertIsInstance(MonsterFactory.get_factory(levels[1]), Level2MonsterFactory)
        self.assertIsInstance(MonsterFactory.get_factory(levels[2]), Level3MonsterFactory)
if __name__ == '__main__':
    # unittest.main()
    ConcreteFactory = MonsterFactory.get_factory(levels[0])
    monster1 = ConcreteFactory.create_monster('Goblin')
    print(monster1.max_health)

