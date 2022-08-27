import Monster
from SmallScriptsAndPrograms import Hero

import random
import pyodbc


class Level:
    def __init__(self, current_cursor: pyodbc.Cursor):
        self.monster_shuffle = {}
        self.current_monster_selected: Monster = None
        self.cursor = current_cursor

    def __select_monster_for_attack(self):
        monster_index = random.randint(0, len(self.monster_shuffle) - 1)
        self.current_monster_selected = self.monster_shuffle[monster_index]

    def receive_hero(self, current_hero: Hero.Hero, current_monster: str):

        current_hero_damage = current_hero.get_hero_damage()

        if current_monster is None:
            value: Monster.Monster

            for monster_name, value in self.monster_shuffle.items():
                print(f"\n{monster_name} has received {current_hero_damage} Damage!\nHP: {value.monster_hp}"
                      f" reduced to {value.monster_hp - current_hero_damage}")

                value.monster_hp -= current_hero_damage

        elif current_monster is not None:

            monster_value: Monster.Monster = self.monster_shuffle[current_monster]

            print(f"\n{current_monster} has received {current_hero_damage} Damage!\nHP: {monster_value.monster_hp}"
                  f" reduced to {monster_value.monster_hp - current_hero_damage}")

            monster_value.monster_hp -= current_hero_damage
    # TODO add the listener class
    def __clear_current_monster(self):
        self.current_monster_selected = None

        if len(self.monster_shuffle) > 0:
            self.__select_monster_for_attack()
        else:
            # add listener pattern for game controller to switch
            pass

    # TODO  figure out how to do it for each level
    def get_monsters_for_level(self):
        self.cursor.execute("SELECT  MONSTER_NAME, MONSTER_HP, MONSTER_DAMAGE, MONSTER_REWARD FROM MONSTERS")

        for monster_item in self.cursor:
            self.monster_shuffle[str(monster_item[0])] = (int(monster_item[1]),
                                                          int(monster_item[2]), float(monster_item[3]))
