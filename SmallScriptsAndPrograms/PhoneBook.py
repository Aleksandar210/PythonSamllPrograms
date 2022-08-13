from collections import defaultdict

phonebook_names = defaultdict(str)


def get_input():
    global phonebook_names

    number_lines_input = int(get_lines_input())

    for _ in range(number_lines_input):
        contact_name, contact_number = input().split("-")
        add_entry(contact_name, contact_number)

    # now we retrieve the input
    number_lines_output = int(get_lines_input())

    for _ in range(number_lines_output):
        contact_name = input()
        contact_info = get_entry(contact_name)
        if contact_info is None:
            print(f"Name {contact_name} not found!!!")
        else:
            print(f"Name: {contact_info[0]} phone number: {contact_info[1]}")


def get_lines_input():
    number_lines = input()

    if number_lines.isdigit():
        return number_lines
    else:
        print("Enter digit 0-9+")
        get_lines_input()


def add_entry(name: str, phone_number: str):
    global phonebook_names

    phonebook_names[name] = phone_number


def get_entry(name: str):
    global phonebook_names

    if name not in phonebook_names.keys():
        return None
    else:
        return name, phonebook_names[name]


# program start
get_input()
