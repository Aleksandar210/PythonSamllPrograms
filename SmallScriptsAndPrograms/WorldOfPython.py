import pyodbc
import random

connection = pyodbc.Connection
cursor = pyodbc.Cursor

OPTION_MENU_STRING = "1|Add new hero!\n2|Delete hero\n3|Start Game\n4|Exit menu!"
OPTION_LEVEL_STRING = None

current_monster_shuffle = {}


def connect_to_server():
    server_name = "localhost"
    database_name = "WorldOfPython"
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server_name + ';DATABASE=' + database_name + ';Trusted_Connection=yes; '

    global connection

    connection = pyodbc.connect(connection_string)

    global cursor
    cursor = connection.cursor()

    global OPTION_MENU_STRING

    while True:
        print(OPTION_MENU_STRING)
        select_command = input("Select command: ")

        if select_command.isdigit():
            match int(select_command):
                case 1:
                    add_new_hero(cursor, connection)
                case 2:
                    delete_hero(cursor, connection)
                case 3:
                    pass
                case 4:
                    print("Good bye!")
                    break
                case other:
                    print("Invalid command please try again!\n")


def add_new_hero(current_cursor: pyodbc.Cursor, current_connection: pyodbc.Connection):
    """
    Description this method prompts the player to enter a name for the hero
    after that the cursor will fetch all the available race_names with their starting stats and prompt the user
    to select a race for the hero based on the available races
    finally the cursor fetches all the available classes and displays them to the user where the method
    prompts the user to enter a class name (select) for the hero

    then the data (name, race, class) is inserted into the database
    """
    hero_name = input("Enter name: ")

    # get race stats so that we can display them to the user
    hero_race_stats = {}
    current_cursor.execute("SELECT HERO_RACE, HERO_RACE_START_HP, HERO_RACE_START_MANA FROM HERO_RACES")
    for item in current_cursor:
        hero_race_stats[str(item[0]).capitalize()] = (str(item[1]), str(item[2]))

    hero_race_option_string = "\n".join(f"{hero_race} -> "
                                        f"{hero_race_stats[hero_race][0]} HP {hero_race_stats[hero_race][0]} MANA"
                                        for hero_race in hero_race_stats.keys())
    # Select the hero race for the hero
    selected_hero_race = ""
    while True:
        print(hero_race_option_string)
        selected_hero_race = input("Select hero race: ").capitalize()
        if selected_hero_race in hero_race_stats.keys():
            break

    # get the classes so that we can display them to the user
    hero_classes = []
    current_cursor.execute("SELECT HERO_CLASS FROM HERO_CLASSES")
    for item in current_cursor:
        hero_classes.append(str(item[0]).capitalize())

    hero_class_option_string = "\n".join(f"|{hero_class_name}|" for hero_class_name in hero_classes)

    # select a class for the user
    selected_hero_class = None
    while True:
        print(hero_class_option_string)
        selected_hero_class = input("Select Hero Class: ").capitalize()
        if selected_hero_class in hero_classes:
            break

    # inserting the new hero
    current_cursor.execute(
        f"INSERT INTO HEROS (HERO_NAME, HERO_CLASS, HERO_RACE)"
        f" VALUES ('{hero_name}','{selected_hero_class}','{selected_hero_race}')")

    # commiting / saving the changes into the database
    current_connection.commit()


def delete_hero(current_cursor: pyodbc.Cursor, current_connection: pyodbc.Connection):
    """
    Description:
    we get with the cursor the available heros in the HEROS table
    we then display the heros and ask the user to select an ID to delete
    And we finally delete the hero from the table
    """
    current_heros = {}

    current_cursor.execute(
        "SELECT HERO_ID, HERO_NAME, HERO_CLASS, HERO_RACE, HERO_HP, HERO_MANA, HERO_LEVEL FROM HEROS")

    for item in current_cursor:
        current_heros[int(item[0])] = (str(item[1]), str(item[2]), str(item[3]),
                                       str(item[4]), str(item[5]), str(item[6]))

    hero_delete_option_string = "\n".join(
        f"{hero_id}| NAME: {current_heros[hero_id][0]} CLASS: {current_heros[hero_id][1]} "
        f"RACE: {current_heros[hero_id][2]} LEVEL: {current_heros[hero_id][5]}"
        for hero_id in current_heros.keys())

    while True:
        print(hero_delete_option_string)
        selected_hero_id = input("Enter hero ID to delete: ")

        if selected_hero_id.isdigit() and int(selected_hero_id) in current_heros.keys():
            current_cursor.execute("DELETE FROM HEROS WHERE HERO_ID = " + selected_hero_id)
            current_connection.commit()
            break
        else:
            continue

# TODO FINISH
def get_monsters_for_leve(current_cursor:pyodbc.Cursor, leve_id: int):
    global current_monster_shuffle

    current_cursor.execute("SELECT MONSTER_ID, MONSTER_NAME, MONSTER_HP, MONSTER_DAMAGE")




def fight_monster(current_cursor: pyodbc.Cursor, current_connection: pyodbc.Connection):



connect_to_server()
