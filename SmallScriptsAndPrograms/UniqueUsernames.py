unique_usernames = set()
all_usernames = list()


def get_input():
    number_lines = int(input())

    global all_usernames
    global unique_usernames

    for _ in range(number_lines):
        enter_username = input()
        all_usernames.append(enter_username)
        unique_usernames.add(enter_username)

    unique_username_string = "\n".join(unique_usernames)
    print(f"Unique Usernames are\n{unique_username_string}")


get_input()
