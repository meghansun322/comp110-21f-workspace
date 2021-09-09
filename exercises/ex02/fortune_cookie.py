"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396963"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")
random_int: int = randint(1, 4)
if (random_int == 1):
    print("You will life a very happy life.")
elif (random_int == 2):
    print("You will see a dark day soon.")
elif (random_int == 3):
    print("Manifest the life you want.")
else:
    print("Good things are going to come.")

print("Now, go spread positive vibes!")
