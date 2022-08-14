multidimensional_array = list()


def get_input():
    height, width = [int(n) for n in input().split()]

    global multidimensional_array

    current_max_sum = 0
    current_max_matrix = list()

    current_three_by_three_matrix = list()

    if validate_matrix(height, width):
        fill_matrix(height)

        for _ in range(len(multidimensional_array) - 2):
            for __ in range(len(multidimensional_array[_]) - 2):

                first_row = multidimensional_array[_][__:__ + 3]
                second_row = multidimensional_array[_ + 1][__:__ + 3]
                third_row = multidimensional_array[_ + 2][__:__ + 3]

                current_three_by_three_matrix = [first_row, second_row, third_row]
                curr_matrix_sum = get_matrix_sum(current_three_by_three_matrix)

                if current_max_sum <= curr_matrix_sum:
                    current_max_sum = curr_matrix_sum
                    current_max_matrix = current_three_by_three_matrix
    else:
        print("Invalid dimensions for array!!!")
        get_input()

    print(
        f"\nMaximum sum: {current_max_sum}\nmatrix is:\n" + f"{current_max_matrix[0]}\n{current_max_matrix[1]}\n{current_max_matrix[2]}\n")


def validate_matrix(height: int, width: int):
    if height >= 3 and width >= 3:
        return True
    else:
        return False


def get_matrix_sum(matrix: list):
    current_sum = 0
    for _ in matrix:
        current_sum += sum(_)

    return current_sum


def fill_matrix(height: int):
    global multidimensional_array

    for _ in range(height):
        multidimensional_array.append([int(n) for n in input().split()])


# program start
get_input()
