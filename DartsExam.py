player_one = []
player_two = []
current_playing_player = ""
dart_board = []
turn_counter = 0
is_game_won = False


def setup():
    global player_one, player_two, dart_board, current_playing_player

    player_one = [input("Enter name for player one: "), 501]
    player_two = [input("Enter name for player two: "), 501]

    for _ in range(7):
        current_row_data = [int(cell_value) if cell_value.isdigit() else str(cell_value)
                            for cell_value in input().split(" ")]

        dart_board.append(current_row_data)
    print(f"Player: {player_one[0]} starts first!")
    current_playing_player = player_one[0]


def play():
    global turn_counter, current_playing_player

    while True:
        turn_counter += 1

        hit_coordinates = [int(coordinate) for coordinate in input().strip("()").split(", ")]

        hit_coordinate(hit_coordinates)

        if is_game_won:
            break

    print(f"Player: {current_playing_player} wins the game! with {turn_counter} turns!")


def hit_coordinate(hit_coordinates: list):
    global dart_board, is_game_won

    def reduce_player_points(points: int):
        global current_playing_player, player_two, player_one, is_game_won

        if player_two[0] == current_playing_player:
            player_two[1] -= points
        else:
            player_one[1] -= points

        if player_two[1] <= 0 or player_one[1] <= 0:
            is_game_won = True

    coordinate_value = dart_board[hit_coordinates[0]][hit_coordinates[1]]

    def get_subordinates():

        first = dart_board[hit_coordinates[0]][0]
        second = dart_board[hit_coordinates[0]][len(dart_board[hit_coordinates[0]]) - 1]
        third = dart_board[0][hit_coordinates[1]]
        fourth = dart_board[len(dart_board) - 1][hit_coordinates[1]]

        return sum([first, second, third, fourth])

    if str(coordinate_value).isdigit():
        reduce_player_points(coordinate_value)
    elif coordinate_value == "D":
        reduce_player_points(get_subordinates() * 2)
    elif coordinate_value == "T":
        reduce_player_points(get_subordinates() * 3)
    elif coordinate_value == "B":
        is_game_won = True


setup()
play()
