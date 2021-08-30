"""Exercise 01."""

__author__ = "730396963"

left: str = input("Left-hand side: ")
right: str = input("Righ-hand side: ")
left_value: int = int(left)
right_value: int = int(right)

print(left + " < " + right + " " + str(left_value < right_value))
print(left + " >= " + right + " " + str(left_value >= right_value))
print(left + " == " + right + " " + str(left_value == right_value))
print(left + " != " + right + " " + str(left_value != right_value))
