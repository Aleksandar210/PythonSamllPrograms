import os

exercise_files_location = os.getcwd() + "\\SmallScriptsAndPrograms" + "\\FileManipulatorExerciseFiles"
current_files = {}


def create_file(file_name: str):
    path_name = exercise_files_location + "\\" + file_name

    if file_name in current_files.keys():
        print("File already exists!!")
    else:
        fp = open(path_name, "x")
        fp.close()
        current_files[file_name] = path_name


def add_to_file(file_name: str, content: str):
    pass


def replace_in_file(file_name: str, content: str):
    pass


def delete_file(file_name: str):
    pass


def start():
    pass

