"""Drawing forests in a loop."""

__author__ = "730396963"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

input_str: str = input("Depth: ")

input_int: int = int(input_str)

counter_1: int = 0

while counter_1 < input_int:
    counter_2: int = 0
    tree_string: str = ""
    while counter_2 < counter_1 + 1:
        tree_string = tree_string + TREE
        counter_2 = counter_2 + 1

    print(tree_string)

    counter_1 = counter_1 + 1
