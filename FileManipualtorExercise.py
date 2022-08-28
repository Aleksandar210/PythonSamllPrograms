import os
from os import walk

exercise_files_location = os.getcwd() + "\\SmallScriptsAndPrograms" + "\\FileManipulatorExerciseFiles"
current_files = {}


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            current_files[file] = os.path.join(path, file)


def create_file(file_name: str):
    path_name = exercise_files_location + "\\" + file_name

    if file_name in current_files.keys():
        print("File already exists!!")
    else:
        fp = open(path_name, "x")
        fp.close()
        current_files[file_name] = path_name


def does_file_exist(file_name: str):
    if file_name in current_files.keys():
        return True
    else:
        return False


def is_file_empty(file_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.stat(file_path).st_size == 0


def add_to_file(file_name: str, content: str):
    """we check first if the file is empty if it is we insert the new content as it is
    if the file is not empty we insert the new content with a new line"""

    # check if file exists
    if does_file_exist(file_name):
        if is_file_empty(current_files[file_name]):
            with open(current_files[file_name], 'a') as fp:
                fp.write(content)
        else:
            with open(current_files[file_name], 'a') as fp:
                fp.write(f"\n{content}")


def replace_in_file(file_name: str, old_string: str, new_string: str):
    # check if file exists
    if does_file_exist(file_name):
        # check if file is empty
        if is_file_empty(current_files[file_name]):
            print(f"File {file_name} does not exist or it is empty!!")
        else:
            # Read in the file
            with open(current_files[file_name], 'r') as file:
                file_content = file.read()

            # Replace the target string
            file_content = file_content.replace(old_string, new_string)

            # Write the file out again
            with open(current_files[file_name], 'w') as file:
                file.write(file_content)
    else:
        print(f"File {file_name} does not exist!!")


def delete_file(file_name: str):
    """We check if the file exists and if so we remove it"""
    if does_file_exist(file_name):
        os.remove(current_files[file_name])
    else:
        print(f"File {file_name} does not exist!!!")


def start():
    while True:
        command = input()
        if command.lower() == "end":
            break
        else:
            command = command.split("-")

            match command[0].lower():
                case "create":
                    create_file(command[1])
                case "add":
                    add_to_file(command[1], command[2])
                case "replace":
                    replace_in_file(command[1], command[2], command[3])
                case "delete":
                    delete_file(command[1])
                case other:
                    print("Command not supported!!!")


get_files(exercise_files_location)
start()
