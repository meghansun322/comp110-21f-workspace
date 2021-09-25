"""List utility functions."""

__author__ = "123456789"


def all(list: list[int], match_number: int) -> bool:
    """Returns whether all integer match the desired integer."""
    if len(list) == 0:
        return False
    i: int = 0
    while i < len(list):
        if(list[i] != match_number):
            return False
        i = i + 1
    return True


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns whether two lists are equal."""
    if(len(list1) != len(list2)):
        return False

    i: int = 0
    while i < len(list1):
        if(list1[i] != list2[i]):
            return False
        i = i + 1

    return True


def max(list: list[int]) -> int:
    """Returns the max value in a list."""
    max: int = list[0]
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i = i + 1

    return max
