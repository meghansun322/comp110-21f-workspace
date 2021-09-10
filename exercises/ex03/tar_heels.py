"""An exercise in remainders and boolean logic."""

__author__ = "730396963"


# Begin your solution here...
input_str: str = input("Enter an int: ")

input_int = int(input_str)

if (input_int % 2 == 0) & (input_int % 7 == 0):
    print("TAR HEELS")
else:
    if(input_int % 2 == 0):
        print("TAR")
    else:
        if(input_int % 7 == 0):
            print("HEELS")
        else:
            print("CAROLINA")
