"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_use_case00() -> None:
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_only_evens_use_case01() -> None:
    x: list[int] = [4, 4, 4] 
    assert only_evens(x) == [4, 4, 4]


def test_only_evens_no_even() -> None:
    x: list[int] = [1, 5, 3]
    assert only_evens(x) == []


def test_sub_use_case00() -> None:
    x: list[int] = [10, 20, 30, 40]
    assert sub(x, 1, 3) == [20, 30]


def test_sub_use_case01() -> None:
    x: list[int] = [10, 20, 30, 40]
    assert sub(x, 0, 3) == [10, 20, 30]


def test_sub_start_neg() -> None:
    x: list[int] = [10, 20, 30, 40]
    assert sub(x, -1, 3) == [10, 20, 30]


def test_sub_end_greater_len() -> None:
    x: list[int] = [10, 20, 30, 40]
    assert sub(x, 1, 9) == [20, 30, 40]    


def test_sub_start_greater_length() -> None:
    x: list[int] = [10, 20, 30, 40]
    assert sub(x, 6, 7) == []


def test_sub_list_is_0() -> None:
    x: list[int] = []
    assert sub(x, 6, 7) == []


def test_sub_end_not_pos() -> None:
    x: list[int] = [10, 20]
    assert sub(x, 6, -1) == []


def test_concat_use_case00() -> None:
    x: list[int] = [10, 20]
    y: list[int] = [30, 40]
    assert concat(x, y) == [10, 20, 30, 40]


def test_concat_use_case01() -> None:
    x: list[int] = [10]
    y: list[int] = [20, 30, 40]
    assert concat(x, y) == [10, 20, 30, 40]


def test_concat_list1_empty() -> None:
    x: list[int] = []
    y: list[int] = [20, 30, 40]
    assert concat(x, y) == [20, 30, 40]


def test_concat_list2_empty() -> None:
    x: list[int] = []
    y: list[int] = [20, 30, 40]
    assert concat(y, x) == [20, 30, 40]


def test_concat_both_empty() -> None:
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []
