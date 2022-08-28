player_one = ()
player_two = ()
starting_player = None
starting_player_sign = " "

playing_board = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]


# make it smarter with condition check for where the player has played
def check_if_won(current_position: int):
    first_row = playing_board[0][0] + playing_board[0][1] + playing_board[0][2]
    second_row = playing_board[1][1] + playing_board[1][1] + playing_board[1][2]
    third_row = playing_board[2][0] + playing_board[2][1] + playing_board[2][2]

    first_down_row = playing_board[0][0] + playing_board[1][0] + playing_board[2][0]
    second_down_row = playing_board[0][1] + playing_board[1][1] + playing_board[2][1]
    third_down_row = playing_board[0][2] + playing_board[1][2] + playing_board[2][2]

    all_rows = [first_row, second_row, third_row, first_down_row, second_down_row, third_down_row]

    # check position
    if current_position in [1, 3, 4, 7, 9]:
        first_diagonal = playing_board[0][1] + playing_board[1][1] + playing_board[2][2]
        second_diagonal = playing_board[0][2] + playing_board[1][1] + playing_board[2][0]
        all_rows.append(first_diagonal)
        all_rows.append(second_diagonal)

    for curr_row in all_rows:
        if check_equal_row(curr_row):
            display_end_message()
            return True

    return False


def display_end_message():
    print(f"PLAYER {starting_player} WINS THE GAME!!!")


def check_equal_row(current_row: str):
    current_row = current_row.lower()
    if current_row == "xxx" or current_row == "ooo":
        return True
    else:
        return False


def play():
    global starting_player

    while True:
        position_picked = input(f"{starting_player} chose a free position from [1-9]: ")

        if position_picked.isdigit():
            position_picked = translate_to_board_position(int(position_picked))

        if position_picked[0] is None and position_picked[1] is None:
            print(f"Invalid Position Please pick a valid position Player {starting_player}")
            continue

        if check_if_position_is_free(position_picked):
            position_picked = tuple(position_picked)
            playing_board[position_picked[0]][position_picked[1]] = starting_player_sign
            print(f"Player {starting_player} picked {position_picked[1] + 1} with the sign {starting_player_sign} ")
            display_board()
            if check_if_won(position_picked[1] + 1):
                break
            else:
                switch_player()


def translate_to_board_position(position_picked: int):
    row_number = None
    col_value = None

    if 1 <= position_picked <= 3:
        row_number = 0
        col_value = position_picked - 1
    elif 4 <= position_picked <= 6:
        row_number = 1
        match position_picked:
            case 4:
                col_value = 0
            case 5:
                col_value = 1
            case 6:
                col_value = 2
    elif 7 <= position_picked <= 9:
        row_number = 2
        match position_picked:
            case 7:
                col_value = 0
            case 8:
                col_value = 1
            case 9:
                col_value = 2
    else:
        return None, None

    return row_number, col_value


def check_if_position_is_free(position: tuple):
    if playing_board[position[0]][position[1]] == " ":
        return True
    else:
        return False


def switch_player():
    global starting_player, starting_player_sign

    if starting_player == player_one[0]:
        starting_player, starting_player_sign = player_two[0], player_two[1]
    else:
        starting_player, starting_player_sign = player_one[0], player_one[1]


def display_board():
    result = ""
    for row_data in playing_board:
        result += "".join(f"| {col_value}" for col_value in row_data) + " |"
        result += "\n"

    print(result)


def setup():
    player_one_name = input("Enter player one name: ")
    player_two_name = input("Enter player two name: ")

    player_one_sign = enter_player_sign(player_one_name)
    player_two_sign = enter_player_sign(player_two_name)

    global player_one, player_two, starting_player, starting_player_sign

    player_one = (player_one_name, player_one_sign)
    player_two = (player_two_name, player_two_sign)

    starting_player = player_one[0]
    starting_player_sign = player_one[1]

    print("This is the numeration for the board: ")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"Player: {starting_player} starts first")


def enter_player_sign(player_name: str):
    player_sign = input(f"Enter sign for player: {player_name} ")

    while True:
        if verify_sign(player_sign):
            break
        else:
            print(f"Sign {player_sign} was invalid acceptable signs are X/O")
            player_sign = input("Enter player one sign")

    return player_sign


def verify_sign(sign: str):
    if sign.lower() == "o" or sign.lower() == "x":
        return True
    else:
        return False


setup()
play()
