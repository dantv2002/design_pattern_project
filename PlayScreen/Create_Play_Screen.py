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

if __name__ == '__main__':
    monster_levels_of_play_screen = [{"level1count": 3},
                                     {"level1count": 2, "level2_count": 1},
                                     {"level1count": 2, "level3_count":1},
                                     {"level1count": 1, "level2_count": 2},
                                     {"level1count": 1, "level2_count": 1, "level3_count": 1},
                                     {"level2count": 3},
                                     {"level2count": 2, "level3_count": 1},
                                     {"level3count": 1, "level2_count": 2},
                                     {"level3count": 2, "level2_count": 1},
                                     {"level3count": 3}]

    # Chọn cấp độ màn chơi
    play_screen_level = 4 #=============================> CHỌN ĐỘ KHÓ <================================
    play_screen = GameLevel_Composite("Play screen " + str(play_screen_level))

    # Tạo quái tương ứng với cấp độ màn chơi
    index = play_screen_level - 1
    temp = monster_levels_of_play_screen[index]
    name_monster = ['Gargoyle', 'Demon', 'Android']
    random.shuffle(name_monster)
    selected = 0 # vị trí chọn tên quái
    if 'level1count' in temp:
        for i in range(temp['level1count']):
            play_screen.add_monster(GameLevel_Leaf(name_monster[selected], 1))
            selected = selected + 1
    if 'level2_count' in temp:
        for i in range(temp['level2_count']):
            play_screen.add_monster(GameLevel_Leaf(name_monster[selected], 2))
            selected = selected + 1
    if 'level3_count' in temp:
        for i in range(temp['level3_count']):
            play_screen.add_monster(GameLevel_Leaf(name_monster[selected], 3))
            selected = selected + 1
    selected = 0

    print('\n=================== '+ 'LIST MONSTER OF ' + str(play_screen.get_name()) + ' ===================\n')
    for monster in play_screen.list_monster:
        print('Name monster: {}'.format(monster.get_name()))
        print('Level monster: {}'.format(monster.get_level()))
        print('Max health monster: {}'.format(monster.get_max_health()))
        print('Coin monster: {}'.format(monster.get_coin()))
        print('===================')