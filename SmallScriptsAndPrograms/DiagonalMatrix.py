multidimensional_array = list()


def get_input() -> "Returns nothing it fills the multidimensional_array (global var)":
    """The function requires the user to enter an integer
    The integer then will be looped and for each line a separated with space
    will add the elements to the multidimensional array"""

    entered_lines = input()

    global multidimensional_array
    if entered_lines.isdigit():
        entered_lines = int(entered_lines)
        for _ in range(entered_lines):
            enter_list_data = [int(n) for n in input().split()]
            multidimensional_array.append(enter_list_data)
    else:
        print("Please enter a digit 0-9 + ")
        get_input()

    primary_diagonal_sum = get_first_diagonal_sum()
    secondary_diagonal_sum = get_last_diagonal_sum()
    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    print(
        f"Primary diagonal sum is: {primary_diagonal_sum}\nSecondary diagonal sum is: {secondary_diagonal_sum}\nDifference is: {difference}")


def get_first_diagonal_sum() -> "returns the diagonal sum":
    """gets the diagonal sum starting from 0 from the first list and ending with the last
    val of the last list"""
    global multidimensional_array
    index = 0
    diagonal_sum = 0
    for _ in range(len(multidimensional_array)):
        diagonal_sum += multidimensional_array[_][index]
        index += 1

    return diagonal_sum


def get_last_diagonal_sum() -> "returns the last diagonal sum from the last element to the first of the first list":
    """gets the diagonal sum starting from len() - 1 from the first list and ending with the first
        val of the last list"""

    global multidimensional_array
    index = len(multidimensional_array[0]) - 1
    diagonal_sum = 0
    for _ in range(len(multidimensional_array)):
        diagonal_sum += multidimensional_array[_][index]
        index -= 1

    return diagonal_sum


get_input()
