current_field = list()
bunny_coordinates = list(tuple)
player_coordinates = [-1, -1]
commands = list()

game_over = False
game_won = False


def get_input():
    height, width = [int(n) for n in input().split()]

    global current_field
    global player_coordinates
    global bunny_coordinates

    for _ in range(height):
        current_line = " ".join(input()).split()
        current_field.append(current_line)

        # check for player position
        if player_coordinates[0] == -1 and player_coordinates[1] == -1:
            try:
                player_cell_value = current_line.index("P")
                player_coordinates = [_, player_cell_value]
            except ValueError:
                pass

        # getting bunny indexes if there are any for the line
        for __ in range(len(current_line)):
            if current_line[__] == "B":
                bunny_coordinates.append((_, __))

    # getting commands
    global commands

    commands = " ".join(input()).split()


def process_commands():
    global commands
    global player_coordinates
    global current_field

    for command in commands:
        match str(command).lower():
            case "l":
                pass
            case "u":
                pass
            case "d":
                pass
            case "r":
                pass


def process_cell_value_player(current_position: tuple):
    global current_field
    global player_coordinates
    global game_over
    global game_won

    cell_value = current_field[current_position[0]][current_position[1]]

    # check if player is outside the filed
    if current_position[0] < 0 or current_position[0] > len(current_field) - 1:
        game_won = True
        return

    if current_position[1] < 0 or current_position[1] > len(current_field[current_position[0]]) - 1:
        game_won = True
        return

    # if player hasn't won check his next cell value
    if cell_value == ".":
        current_field[player_coordinates[0]][player_coordinates[1]] = "."
        current_field[current_position[0]][current_position[1]] = "P"
    elif cell_value == "B":
        game_over = True


def process_cell_value_bunny(current_bunny_coordinate: tuple, new_bunny_coordinates: list):
    global current_field

    cell_value = current_field[current_bunny_coordinate[0]][current_bunny_coordinate[1]]

    global game_over
    if cell_value == "P":
        game_over = True

    current_field[current_bunny_coordinate[0]][current_bunny_coordinate[1]] = "B"

    # we add the current_bunny to the new list
    new_bunny_coordinates.append(current_bunny_coordinate)


def spread_bunnies():
    new_bunnies_location = list()

    global bunny_coordinates
    global current_field

    for _ in range(len(bunny_coordinates)):
        current_bunny_coordinate = bunny_coordinates.pop()
        # check bunny coordinate
        if current_bunny_coordinate[0] == 0 and \
                (0 < current_bunny_coordinate[1] < len(current_field[current_bunny_coordinate[0]]) - 1):
            pass
        elif current_bunny_coordinate[0] == 0 and (current_bunny_coordinate[1] == 0):
            pass
        elif current_bunny_coordinate[0] == len(current_field) - 1 and\
                (0 < current_bunny_coordinate[1] < len(current_field[current_bunny_coordinate[0]]) - 1):
            pass
        elif 0 < current_bunny_coordinate[0] < len(current_field) - 1:
            if current_bunny_coordinate[1] == 0:
                pass
            elif current_bunny_coordinate[1] == len(current_field[current_bunny_coordinate[0]]) - 1:
                pass
            elif 0 < current_bunny_coordinate[1] < len(current_field[current_bunny_coordinate[0]]) - 1:
                pass




