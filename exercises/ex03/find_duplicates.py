"""Finding duplicate letters in a word."""

__author__ = "730396963"

input: str = input("Enter a word: ")

is_duplicate: bool = False
tracker_1: int = 0

while tracker_1 < len(input):
    tracker_2: int = tracker_1 + 1
    current_char: str = input[tracker_1]
    while tracker_2 < len(input):
        if (current_char == input[tracker_2]):
            is_duplicate = True

        tracker_2 = tracker_2 + 1

    tracker_1 = tracker_1 + 1

print("Found duplicate: " + str(is_duplicate))
