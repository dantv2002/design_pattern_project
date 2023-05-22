import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
import_path = os.path.join(current_dir, 'GameLevel')
sys.path.insert(0, import_path)
import_path = os.path.join(current_dir, 'Monster')
sys.path.insert(0, import_path)
from GameLevel_Composite import GameLevel_Composite
from GameLevel_Leaf import GameLevel_Leaf
import random

class Create_Play_Screen:
    __MONSTER_LEVELS_OF_PLAY_SCREEN = [{"level1count": 3},
                                     {"level1count": 2, "level2count": 1},
                                     {"level1count": 2, "level3count":1},
                                     {"level1count": 1, "level2count": 2},
                                     {"level1count": 1, "level2count": 1, "level3count": 1},
                                     {"level2count": 3},
                                     {"level2count": 2, "level3count": 1},
                                     {"level3count": 1, "level2count": 2},
                                     {"level3count": 2, "level2count": 1},
                                     {"level3count": 3}]
    def __init__(self, play_screen_level):
        self.__play_screen_level = play_screen_level
    
    def create(self):
        play_screen = GameLevel_Composite("Play screen " + str(self.__play_screen_level))
        # Tạo quái tương ứng với cấp độ màn chơi
        index = self.__play_screen_level - 1
        temp = self.__MONSTER_LEVELS_OF_PLAY_SCREEN[index]
        name_monster = ['Gargoyle', 'Demon', 'Android']
        random.shuffle(name_monster)
        selected = 0 # vị trí chọn tên quái
        if 'level1count' in temp:
            for i in range(temp['level1count']):
                play_screen.add_monster(GameLevel_Leaf(name_monster[selected], 1))
                selected = selected + 1
        if 'level2count' in temp:
            for i in range(temp['level2count']):
                play_screen.add_monster(GameLevel_Leaf(name_monster[selected], 2))
                selected = selected + 1
        if 'level3count' in temp:
            for i in range(temp['level3count']):
                play_screen.add_monster(GameLevel_Leaf(name_monster[selected], 3))
                selected = selected + 1
        return play_screen




if __name__ == '__main__':
    # TEST tạo màn chơi
    create_play_screen = Create_Play_Screen(play_screen_level=6)
    play_screen = create_play_screen.create()
    # Hiển thị kết quả TEST
    print('\n=================== '+ 'LIST MONSTER OF ' + str(play_screen.get_name()) + ' ===================\n')
    for monster in play_screen.list_monster:
        print('Name monster: {}'.format(monster.get_name()))
        print('Level monster: {}'.format(monster.get_level()))
        print('Max health monster: {}'.format(monster.get_max_health()))
        print('Coin monster: {}'.format(monster.get_coin()))
        print('===================')
    monster1 = play_screen.list_monster[0]
    monster2 = play_screen.list_monster[1]
    monster3 = play_screen.list_monster[2]

    monster1.set_max_health(0)
    monster2.set_coin(0)
    monster3.set_coin(100)
    monster3.set_max_health(100)
    print()
    for monster in play_screen.list_monster:
        print('Name monster: {}'.format(monster.get_name()))
        print('Level monster: {}'.format(monster.get_level()))
        print('Max health monster: {}'.format(monster.get_max_health()))
        print('Coin monster: {}'.format(monster.get_coin()))
        print('===================')
    