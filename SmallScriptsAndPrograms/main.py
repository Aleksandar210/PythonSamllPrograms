import pyodbc

current_user_name = "Aleksandar Kuzmov"

def sql_server_test():
    server_name = 'localhost'  # Your server name
    database_name = 'WorldOfPython'  # Your database name
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server_name + ';DATABASE=' + database_name + ';Trusted_Connection=yes; '

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM HEROS')

    for item in cursor.fetchall():
        hero_name, hero_race, hp_points, mana_points = item[1], item[3], item[4], item[5]
        if hero_race == "Android":
            print(f"{hero_name} is an Android with {hp_points} HP points and {mana_points} Mana points")

def print_hi(name):
    """
    Description of function:
    print_hi functions accepts a str parameter and prints Hi, to that parameter
    to the console

    Arguments:
        name(str) this represents the name that will be used to say Hi to
    """
    print(f'Hi, {name}')


if __name__ == '__main__':
    print("current_user: " + current_user_name)


