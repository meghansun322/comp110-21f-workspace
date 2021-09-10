"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

input: int = int(input("Depth: "))

counter_1: int = 0

while counter_1 < input:
    counter_2: int = 0
    tree_string: str = ""
    while counter_2 < counter_1 + 1:
        tree_string = tree_string + TREE
        counter_2 = counter_2 + 1

    print(tree_string)

    counter_1 = counter_1 + 1
