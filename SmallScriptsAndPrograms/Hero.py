import Ability


class Hero:
    def __init__(self, hero_name, hero_class, hero_race, hero_hp, hero_mana, hero_level):
        self.ability: Ability = None
        self.hero_name = hero_name
        self.hero_class = hero_class
        self.hero_race = hero_race
        self.hero_hp = hero_hp
        self.hero_mana = hero_mana
        self.hero_level = hero_level

    def get_hero_damage(self) -> int:
        ability_damage = self.ability.ability_damage
        return ability_damage

    def set_ability(self, current_ability: Ability):
        self.ability = current_ability


