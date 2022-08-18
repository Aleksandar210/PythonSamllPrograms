bomb_coordinates = list()


def get_input():
    height = input()

    if height.isdigit():
        height = int(height)
        fill_array(height)
        get_bomb_coordinates()
    else:
        print("Please enter digits 0-9+")


def fill_array(height: int):
    global multidimensional_array

    for _ in range(height):
        multidimensional_array.append([int(n) for n in input().split()])


def get_bomb_coordinates():
    entered_bomb_coordinates = input().split()

    global bomb_coordinates
    for _ in range(len(entered_bomb_coordinates)):
        row, cell = [int(n) for n in entered_bomb_coordinates[_].split(",")]
        bomb_coordinates.append([row, cell])


def explode_all_bomb():
    global bomb_coordinates
    global multidimensional_array

    for coordinates in bomb_coordinates:
        # main_diagonal_explosion algorithm
        pass


def explode_main_diagonal(current_bomb_coordinates: tuple):
    global multidimensional_array

    current_bomb_value = multidimensional_array[current_bomb_coordinates[0]][current_bomb_coordinates[1]]
    current_height, current_cell = current_bomb_coordinates[0], current_bomb_coordinates[1]

    # check if coordinate of bomb is at start or at end
    if current_height > len(multidimensional_array) - 1 and current_cell != len(
            multidimensional_array[current_height]) - 1:
        index = current_cell + 1
        for _ in range(1, len(multidimensional_array)):
            multidimensional_array[_][index] -= current_bomb_value
            index += 1


def explode_secondary_diagonal(current_bomb_coordinates: list):
    pass


def explode_upp_low_bombs(current_bomb_coordinates: list):
    pass


def explode_side_bombs(current_bomb_coordinates: list):
    pass


def get_alive_cells_data():
    pass


multidimensional_array = [[1, 1, 1, 1, 17], [2, 4, 5, 2, 44], [2, 4, 7, 4, 41], [5, 3, 2, 5, 32]]
for current_list in multidimensional_array:
    print(current_list)

test_bomb_cooridnates_1 = 1, 1
test_bomb_cooridnates_2 = 0, 0
test_bomb_cooridnates_3 = 3, 4

explode_main_diagonal(test_bomb_cooridnates_1)
explode_main_diagonal(test_bomb_cooridnates_2)
explode_main_diagonal(test_bomb_cooridnates_3)


