multidimensional_array = list()


def get_input():
    height, width = [int(n) for n in input().split()]
    count = 0
    if validate_array(height, width):
        fill_array(height)
        for _ in range(len(multidimensional_array) - 1):
            for __ in range(len(multidimensional_array[_]) - 1):
                first, second = multidimensional_array[_][__], multidimensional_array[_][__ + 1]
                third, fourth = multidimensional_array[_ + 1][__], multidimensional_array[_ + 1][__ + 1]
                if first == second and first == third and first == fourth:
                    count += 1
                    print(f"{first} {second}\n{third} {fourth}\n")
    else:
        print("Invalid Matrix dimensions!!!")
        get_input()

    print(count)


def validate_array(height: int, width: int) -> "Validates if the array is at least 2 by 2":
    global multidimensional_array

    if height >= 2 and width >= 2:
        return True
    else:
        return False


def fill_array(height: int) -> "Fills the array with data":
    global multidimensional_array
    for _ in range(height):
        entered_line_data = input().split()
        multidimensional_array.append(entered_line_data)


# program start
# this is my favourite soft uni task
get_input()
