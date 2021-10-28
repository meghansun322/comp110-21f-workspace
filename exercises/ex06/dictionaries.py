"""Practice with dictionaries."""

__author__ = "123456789"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, returns a dictionary that inverts key and value."""
    invert_dict: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] in invert_dict:
            raise KeyError("Dictionary contains multiple identical values")
        else:
            invert_dict[dictionary[key]] = key
    return invert_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the color of most popular color given a dictionary."""
    favorite: str = ""
    color_tracker: dict[str, int] = dict()
    for key in dictionary:
        if dictionary[key] in color_tracker:
            color_tracker[dictionary[key]] = color_tracker[dictionary[key]] + 1
        else:
            color_tracker[dictionary[key]] = 1

    highest: int = 0
    for key in color_tracker:
        if color_tracker[key] > highest:
            highest = color_tracker[key]
            favorite = key

    if (favorite == ""):
        return "no colors found"
    else:
        return favorite


def count(counter: list[str]) -> dict[str, int]:
    """Returns a dictionary of the counts of values for each item of input."""
    dictionary: dict[str, int] = dict()

    for value in counter:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1
    return dictionary
