import Monster
from SmallScriptsAndPrograms import Hero
from typing import Type
from collections import defaultdict
import random


class Level:
    def __init__(self):
        self.monster_shuffle = {}
        self.current_monster_selected: Monster = None

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

    def clear_current_monster(self):
        pass





