person_information = list()


def get_input():
    global person_information

    number_lines = input()
    if number_lines.isdigit():
        for _ in range(int(number_lines)):
            get_text = input()
            add_information(get_name(get_text), get_age(get_text))
    else:
        print("Enter number of lines as integer!!!")
        get_input()

    print_result()


def get_name(string: str):
    name_starting_index = string.find("@")
    name_ending_index = string.find("|")

    if name_ending_index != -1 and name_starting_index != -1:
        return string[name_starting_index + 1:name_ending_index]
    else:
        return None


def get_age(string: str):
    age_starting_index = string.find("#")
    age_ending_index = string.find("*")

    if age_starting_index != -1 and age_ending_index != -1:
        return string[age_starting_index + 1:age_ending_index]
    else:
        return None


def add_information(name: str, age: str):
    global person_information

    if name is None:
        name = "MISSING_NAME"
    if age is None:
        age = "MISSING_AGE"

    person_information.append(f"Hello my name is {name} and I am {age} years old")


def print_result():
    global person_information

    result = "Person information: \n"
    result += "\n".join(person_information)

    print(result)


# start program here
get_input()

