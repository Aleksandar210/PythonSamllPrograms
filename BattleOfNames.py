from collections import defaultdict

names_ascii_sums = defaultdict(list)


def get_lines_input():
    number_lines = input()

    if number_lines.isdigit():
        return int(number_lines)
    else:
        print("Enter digit 0-9+")
        get_lines_input()


def get_ascii_sum(string: str):
    sum_characters = 0

    for _ in string:
        sum_characters += int(_)

    return sum_characters


def get_input():
    number_lines_input = get_lines_input()

    global names_ascii_sums
    names_ascii_sums["odd"] = list()
    names_ascii_sums["even"] = list()

    for _ in range(number_lines_input):
        name_entered = input()
        ascii_sum = get_ascii_sum(name_entered)

        if ascii_sum % 2 == 0:
            names_ascii_sums["even"].append(ascii_sum)
        else:
            names_ascii_sums["odd"].append(ascii_sum)


def process_results():
    global names_ascii_sums
    odd_sum = sum(names_ascii_sums["odd"])
    even_sum = sum(names_ascii_sums["even"])

    if odd_sum == even_sum:
        union_sum = *odd_sum, *even_sum
        print(union_sum)
    elif odd_sum > even_sum:
        print(set.difference(set(names_ascii_sums["odd"]), set(names_ascii_sums["even"])))
    else:
        print(set.symmetric_difference(set(names_ascii_sums["odd"]), set(names_ascii_sums["even"])))


get_input()
process_results()
