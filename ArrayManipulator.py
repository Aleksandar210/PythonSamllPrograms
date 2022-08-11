current_array = []


def fill_array():
    global current_array
    current_array = [int(num) for num in input().strip().split()]


def start_program_function():
    fill_array()
    while True:
        entered_command = input()

        if entered_command.lower() == "end":
            break
        else:
            command_tokens = entered_command.split()
            process_commands(command_tokens)

    global current_array

    print(current_array)


def process_commands(command_given: list):
    global current_array
    match (command_given[0].lower()):
        case "exchange":
            if 0 <= int(command_given[1]) < len(current_array):
                exchange_command(int(command_given[1]))
            else:
                print("Invalid index")
        case "max":
            max_function(command_given[1])
        case "min":
            min_function(command_given[1])
        case "first":
            number_elements = int(command_given[1])
            if number_elements > len(current_array):
                print("Invalid count")
            else:
                first_function(number_elements, command_given[2])
        case "last":
            number_elements = int(command_given[1])
            if number_elements > len(current_array):
                print("Invalid count")
            else:
                last_function(number_elements, command_given[2])


def exchange_command(index: int):
    global current_array
    part_to_exchange = current_array[index + 1::]
    current_array = part_to_exchange + current_array[0:index + 1]


def max_function(number_type: str):
    global current_array

    filtered = list()

    if number_type.lower() == "even":
        filtered = get_even_elements()
    elif number_type.lower() == "odd":
        filtered = get_odd_elements()

    if len(filtered) == 0:
        print("No matches")
    elif len(filtered) != 0:
        max_element = max(filtered)
        print(get_last_index_of_element(max_element, filtered))


def min_function(number_type: str):
    global current_array

    filtered = list()

    if number_type.lower() == "even":
        filtered = get_even_elements()
    elif number_type.lower() == "odd":
        filtered = get_odd_elements()

    if len(filtered) == 0:
        print("No matches")
    elif len(filtered) != 0:
        min_element = min(filtered)
        print(get_last_index_of_element(min_element, filtered))


def first_function(number_elements: int, number_type: str):
    global current_array
    filtered = list()
    if number_type.lower() == "odd":
        filtered = get_odd_elements()
    elif number_type.lower() == "even":
        filtered = get_even_elements()

    if len(filtered) == 0:
        print(filtered)
    elif len(filtered) != 0:
        print(filtered[0:number_elements])


def last_function(number_elements: int, number_type: str):
    global current_array
    filtered = list()
    if number_type.lower() == "even":
        filtered = get_even_elements()
    elif number_type.lower() == "odd":
        filtered = get_odd_elements()

    if len(filtered) == 0:
        print(filtered)
    elif len(filtered) != 0:
        print(filtered[(number_elements * -1):0])


def get_odd_elements():
    global current_array
    filtered = list(filter(lambda number: number % 2 != 0, current_array))
    return filtered


def get_even_elements():
    global current_array
    filtered = list(filter(lambda number: number % 2 == 0, current_array))
    return filtered


def get_last_index_of_element(element: int, elements_list: list):
    times_element_in_list = elements_list.count(element)

    if times_element_in_list > 1:
        for i in range(len(elements_list) - 1, -1, -1):
            if elements_list[i] == element:
                return i
    else:
        return elements_list.index(element)


# we start the program from here!!!
start_program_function()
