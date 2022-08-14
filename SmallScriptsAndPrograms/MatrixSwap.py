multidimensional_array = list()


def get_input():
    height, width = [int(n) for n in input().split()]

    fill_array(height)

    while True:
        command = input()
        if command.lower() == "end":
            break
        else:
            if command.find("swap") >= -1:
                command_tokens = command.split()
                if len(command_tokens) != 5:
                    print("Invalid input")
                else:
                    first_row, first_cell = command_tokens[1], command_tokens[2]
                    second_row, second_cell = command_tokens[3], command_tokens[4]
                    if validate_coordinate(first_row, first_cell, second_row, second_cell):
                        swap_elements(first_row, first_cell, second_row, second_cell)
                        print(get_array_string())
                    else:
                        print("Invalid command")


def fill_array(height: int):
    global multidimensional_array

    for _ in range(height):
        row_data = input().split()
        multidimensional_array.append(row_data)


def validate_coordinate(*args):
    global multidimensional_array

    first_row, first_cell = int(args[0]), int(args[1])
    second_row, second_cell = int(args[2]), int(args[3])

    array_height = len(multidimensional_array) - 1

    if 0 <= first_row <= array_height:
        first_row_length = len(multidimensional_array[first_row])
        if 0 <= first_cell <= first_row_length - 1:
            pass
        else:
            return False
    else:
        return False

    if 0 <= second_row <= array_height:
        second_row_length = len(multidimensional_array[second_row])
        if 0 <= second_cell <= second_row_length - 1:
            pass
        else:
            return False
    else:
        return False

    return True


def swap_elements(*args):
    global multidimensional_array

    first_row, first_cell = int(args[0]), int(args[1])
    second_row, second_cell = int(args[2]), int(args[3])

    multidimensional_array[first_row][first_cell], multidimensional_array[second_row][second_cell] = \
        multidimensional_array[second_row][second_cell], multidimensional_array[first_row][first_cell]


def get_array_string():
    global multidimensional_array

    result = ""

    for _ in range(len(multidimensional_array)):
        result += ",".join(element for element in multidimensional_array[_])

    return result


get_input()
