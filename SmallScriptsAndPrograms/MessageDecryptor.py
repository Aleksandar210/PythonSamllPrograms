from collections import defaultdict

keys = []
decrypted_messages = []

# findings will be a dict with
# Example: gold -> coordinate1, coordinate2, coordinate3 etc
findings = defaultdict(list)


def get_input():
    global keys
    keys = [int(number) for number in input().split()]

    global decrypted_messages

    while True:
        message_entered = input()
        if message_entered.lower() == "find":
            get_statistics()
        else:
            decrypt_messages(message_entered)


def decrypt_messages(current_message: str):
    global keys
    keys_list_len = len(keys)
    counter = 0

    global decrypted_messages

    decrypted_message = ""
    for letter in current_message:
        decrypted_message += chr(ord(letter) - keys[counter])
        counter += 1
        if counter == keys_list_len:
            counter = 0

    decrypted_messages.append(decrypted_message)
    process_decrypted_message(decrypted_message)


def process_decrypted_message(decrypted_message: str):
    global findings

    treasure_type_start_index = decrypted_message.find("&")
    treasure_type_end_index = decrypted_message.find("&", treasure_type_start_index + 1)
    treasure_type = decrypted_message[treasure_type_start_index + 1:treasure_type_end_index]

    coordinates_staring_index = decrypted_message.find("<")
    coordinates_ending_index = decrypted_message.find(">")
    coordinates = decrypted_message[coordinates_staring_index + 1:coordinates_ending_index]

    findings[treasure_type].append(coordinates)


def get_statistics():
    global findings

    coordinate_information = ""
    for treasure_type, coordinates in findings.items():
        coordinate_information += f"Treasure {treasure_type} can be found at:\n"
        for coordinate in coordinates:
            coordinate_information += f" -coordinate: {coordinate}\n"

        coordinate_information += "\n" + ("-" * 10) + "\n\n"

    decrypted_messages_information = ""
    global decrypted_messages

    for message in decrypted_messages:
        decrypted_messages_information += f"Decrypted_message: {message}\n"

    # printing the information
    print(coordinate_information)
    print(decrypted_messages_information)

# start of program
get_input()

