filepath = "todos.txt"


def get_todos(filepath):
    """Reads the todos from the file at filepath, returns them as a list of strings"""

    with open(filepath, 'r') as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(filepath, new_todos_list):
    """Writes the todos to the file at filepath"""

    with open(filepath, 'w') as file:
        file.writelines(new_todos_list)


if __name__ == "__main__":
    print("Hello World\n")
    print(get_todos(filepath), "\n")
    for item in get_todos(filepath):
        print(item.strip("\n"))
