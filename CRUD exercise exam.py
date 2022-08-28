playing_ground = []
current_position = []


def setup():
    global playing_ground, current_position

    for row_index in range(6):
        playing_ground.append(input().split())

    current_position = [int(pos) for pos in input().strip("()").split(", ")]


def play():
    while True:

        command = input()

        if command.lower() == "stop":
            break
        else:
            command_tokens = command.split(", ")
            match command_tokens[0].lower():
                case "create":
                    move_next_position(command_tokens[1])
                    create_command(command_tokens[2])
                case "update":
                    move_next_position(command_tokens[1])
                    update_command(command_tokens[2])
                case "delete":
                    move_next_position(command_tokens[1])
                    delete_command()
                case "read":
                    move_next_position(command_tokens[1])
                    read_command()


def display_playing_board():
    result = ""

    for _ in range(len(playing_ground)):
        result += "".join(value for value in playing_ground[_])
        result += "\n"

    print(result)


def move_next_position(position: str):
    global current_position
    match position.lower():
        case "up":
            current_position[0] -= 1
        case "down":
            current_position[0] += 1
        case "right":
            current_position[1] += 1
        case "left":
            current_position[1] -= 1


def create_command(value: str):
    global playing_ground

    position_value = playing_ground[current_position[0]][current_position[1]]

    if position_value == ".":
        playing_ground[current_position[0]][current_position[1]] = value


def update_command(value: str):
    global playing_ground

    position_value = playing_ground[current_position[0]][current_position[1]]
    if position_value != ".":
        playing_ground[current_position[0]][current_position[1]] = value


def delete_command():
    global playing_ground

    position_value = playing_ground[current_position[0]][current_position[1]]
    if position_value != ".":
        playing_ground[current_position[0]][current_position[1]] = "."


def read_command():
    global playing_ground

    position_value = playing_ground[current_position[0]][current_position[1]]
    if position_value != ".":
        print(position_value)


setup()
play()
display_playing_board()
