"""An exercise in remainders and boolean logic."""

__author__ = "730396963"


# Begin your solution here...
input: int = int(input("Enter an int: "))
if (input % 2 == 0) & (input % 7 == 0):
    print("TAR HEELS")
else:
    if(input % 2 == 0):
        print("TAR")
    else:
        if(input % 7 == 0):
            print("HEELS")
        else:
            print("CAROLINA")
