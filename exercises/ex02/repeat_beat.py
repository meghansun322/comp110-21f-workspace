"""Repeating a beat in a loop."""

__author__ = "730396963"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
repeat: str = input("How many times do you want to repeat it? ")

repeat_int: int = int(repeat)
printed_str: str = ""
if repeat_int <= 0:
    print("No beat...")
else:
    i: int = 0
    while i < repeat_int:
        printed_str += beat
        i = i + 1
        if i < repeat_int:
            printed_str += " "

print(printed_str)
