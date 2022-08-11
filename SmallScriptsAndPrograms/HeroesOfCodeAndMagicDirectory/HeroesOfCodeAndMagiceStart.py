import os

# current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
CURR_HEROES_FILE_NAME = "\\Heroes.txt"

CURR_HERO_NAMES = {}
CURR_MONSTERS = {}

CURR_HEROES_SELECTED = {}


def get_heroes_names():
    file_path = CURR_DIR + CURR_HEROES_FILE_NAME
    heroes_names_list = []

    with open(file_path, 'r') as file:
        heroes_names_list = file.readlines()

    global CURR_HERO_NAMES
    for hero in heroes_names_list:
        hero_name, hero_hp, hero_mp = tuple(hero.split())
        CURR_HERO_NAMES[hero_name] = [int(hero_hp), int(hero_mp)]


def create_file(file_name: str):
    """
    Description:
    check if the text file with the hero information
    exists IF it does the function ends.
    If it does not exist it creates the file
    """
    file_path = CURR_DIR + "\\" + file_name + ".txt"

    if os.path.exists(file_path):
        pass
    else:
        with open(file_path, 'w') as fp:
            print(f"File {file_name}.txt was created!")


def clear_file(file_name: str):
    open(CURR_DIR + "\\" + file_name + ".txt", 'w').close()


def add_hero_data(hero_name: str, hit_points: int, mana_points: int):
    # check if hero name already exists
    global CURR_HERO_NAMES
    current_hero_names = set(CURR_HERO_NAMES.keys())

    if hero_name.capitalize() in current_hero_names:
        print(f"Hero: {hero_name} already exists in the {CURR_HEROES_FILE_NAME} file!")
    else:
        file_path = CURR_DIR + CURR_HEROES_FILE_NAME
        fp = open(file_path, "a")
        # check if file already has names
        if len(CURR_HERO_NAMES) != 0:
            fp.write(f"\n{hero_name.capitalize()} {hit_points} {mana_points}")
        else:
            fp.write(f"{hero_name.capitalize()} {hit_points} {mana_points}")

        fp.close()
        CURR_HERO_NAMES[hero_name.capitalize()] = [int(hit_points), int(mana_points)]
        print(f"New Hero has been added: {hero_name} HP: {hit_points} MP: {mana_points}")


def add_monster(monster_name: str, hit_points: int):
    global CURR_MONSTERS
    current_monster_names = set(CURR_MONSTERS.keys())

    if monster_name.capitalize() in current_monster_names:
        print(f"Monster: {monster_name} already exists in the Monsters.txt file!")
    else:
        file_path = CURR_DIR + "\\Monsters.txt"
        fp = open(file_path, "a")
        # check if file already has names
        if len(CURR_MONSTERS) != 0:
            fp.write(f"\n{monster_name.capitalize()} {hit_points}")
        else:
            fp.write(f"{monster_name.capitalize()} {hit_points}")

        fp.close()
        CURR_MONSTERS[monster_name.capitalize()] = int(hit_points)
        print(f"Monster has been added: {monster_name} HP: {hit_points}")


def pick_heroes():
    global CURR_HERO_NAMES
    global CURR_HEROES_SELECTED

    print('\n' * 2)
    for hero_name, hero_data in CURR_HERO_NAMES.items():
        print(f" {hero_name} - HP: {hero_data[0]} MP: {hero_data[1]}")

    selected_hero = input("\nSelect hero by his name: ").capitalize()

    if selected_hero.lower() == "end":
        return
    else:
        if selected_hero in set(CURR_HERO_NAMES.keys()):
            hero_name = selected_hero
            hero_hp = CURR_HERO_NAMES[selected_hero][0]
            hero_mp = CURR_HERO_NAMES[selected_hero][1]

            CURR_HEROES_SELECTED[hero_name] = [hero_hp, hero_mp]
            CURR_HERO_NAMES.pop(selected_hero)

            print(f"Hero: {selected_hero} was selected for the journey!")
        else:
            print(f"\n\n\n Hero {selected_hero} not found Try again!")

        pick_heroes()


create_file("Heroes")
create_file("Spells")
create_file("Monsters")

get_heroes_names()

# add monsters to file and dictionary
# first we clean the file so that we do not add any dub data
clear_file("Monsters")

add_monster("Fire_Dragon", 100)
add_monster("Undead_Warrior", 59)
add_monster("Undead_Wizard", 80)
add_monster("Spider", 80)
add_monster("Assassin_Servant", 100)
add_monster("Giant", 200)
add_monster("Fire_Horse", 300)
add_monster("Desert_Warrior", 179)
add_monster("Ice_Yeti", 500)


print(f"{len(CURR_MONSTERS)} Monsters have been added!")


