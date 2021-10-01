"""List utility functions part 2."""

__author__ = "123456789"


def only_evens(nums: list[int]) -> list[int]:
    """Keep the evens."""
    evens: list[int] = []
    for number in nums:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Return list of numbers from desired index range."""
    if(len(nums) == 0 or start > len(nums) or end <= 0):
        return []

    if(start < 0):
        start = 0

    if(end > len(nums)):
        end = len(nums)

    new_list: list[int] = []
    i: int = start
    while i < end:
        new_list.append(nums[i])
        i = i + 1
    return new_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Return combined list of numbers."""
    concat_list: list[int] = list_1
    for numbers in list_2:
        concat_list.append(numbers)
    return concat_list
