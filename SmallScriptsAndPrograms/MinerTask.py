miner_field = list()
commands = list()

coals_collected = 0
total_coals = 0
end_game = False

miner_current_position = [-1, -1]


def get_input():
    # getting input size
    field_size = input()
    if field_size.isdigit():
        field_size = int(field_size)
    else:
        print("Enter digit field size 0-9+")
        get_input()

    # getting commands
    global commands
    commands = input().split()
    fill_array(field_size)


def process_commands():
    global commands
    global total_coals
    global coals_collected
    global end_game

    result_message = None

    for command in commands:
        match str(command).lower():
            case "up":
                command_up()
            case "down":
                command_down()
            case "left":
                command_left()
            case "right":
                command_right()

        if end_game:
            if coals_collected == total_coals:
                result_message = f"You collected all coals! ({miner_current_position[0]}, {miner_current_position[1]})."
            else:
                result_message = f"Game over! ({miner_current_position[0]}, {miner_current_position[1]})."

    if result_message is None:
        result_message = f"{total_coals - coals_collected} coals left. ({miner_current_position[0]}, {miner_current_position[1]})."

    print(result_message)


def fill_array(field_size: int):
    global miner_field
    global total_coals

    for _ in range(field_size):
        current_line = input().split()
        miner_field.append(current_line)

        # getting count of the coals if there are any
        coal_count = current_line.count("c")
        if coal_count > 0:
            total_coals += coal_count

        if miner_current_position[0] == -1 and miner_current_position[1] == -1:
            # checking if current line contains the start of the miner
            try:
                starting_position = current_line.index("s")
                miner_current_position[0], miner_current_position[1] = _, starting_position
            except ValueError:
                # handle ValueError exception
                pass


def process_current_cell(current_position: tuple):
    global miner_field

    cell_value = miner_field[current_position[0]][current_position[1]]

    global coals_collected
    global end_game
    global total_coals
    match cell_value.lower():
        case "*":
            pass
        case "c":
            coals_collected += 1
            miner_field[current_position[0]][current_position[1]] = "*"
            if coals_collected == total_coals:
                end_game = True

        case "e":
            end_game = True


def command_up():
    global miner_current_position

    miner_current_position[0] -= 1

    if miner_current_position[0] < 0:
        miner_current_position[0] += 1
    else:
        process_current_cell(tuple(miner_current_position))


def command_down():
    global miner_current_position
    global miner_field

    miner_current_position[0] += 1

    if miner_current_position[0] > len(miner_field) - 1:
        miner_current_position[0] -= 1
    else:
        process_current_cell(tuple(miner_current_position))


def command_left():
    global miner_current_position

    miner_current_position[1] -= 1

    if miner_current_position[1] < 0:
        miner_current_position[1] += 1
    else:
        process_current_cell(tuple(miner_current_position))


def command_right():
    global miner_field
    global miner_current_position

    miner_current_position[1] += 1

    if miner_current_position[1] > len(miner_field[miner_current_position[0]]) - 1:
        miner_current_position[1] -= 1
    else:
        process_current_cell(tuple(miner_current_position))


# program start
get_input()
print()
process_commands()
# end of program
