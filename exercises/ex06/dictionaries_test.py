"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest

__author__ = "123456789"


def test_invert_use_case_00() -> None:
    """Test."""
    d: dict[str, str] = {
        'a': 'z',
        'b': 'y',
        'c': 'x'
    }
    assert invert(d) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_case_01() -> None:
    """Test."""
    d: dict[str, str] = {'apple': 'cat'}
    assert invert(d) == {'cat': 'apple'}


def test_invert_same_key() -> None:
    """Test."""
    d: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError):
        invert(d)


def test_invert_use_empty() -> None:
    """Test."""
    d: dict[str, str] = {}
    assert invert(d) == {}


def test_favorite_color_use_case_00() -> None:
    """Test."""
    d: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(d) == "blue"


def test_favorite_color_use_case_01() -> None:
    """Test."""
    d: dict[str, str] = {"Marc": "yellow", "Ezri": "red", "Kris": "blue"}
    assert favorite_color(d) == "yellow"


def test_favorite_color_use_case_02() -> None:
    """Test."""
    d: dict[str, str] = {"Marc": "red", "Ezri": "red", "Kris": "red"}
    assert favorite_color(d) == "red"


def test_favorite_color_empty() -> None:
    """Test."""
    d = dict()
    assert favorite_color(d) == "no colors found"


def test_count_use_case_00() -> None:
    """Test."""
    str_list: list[str] = ["h", "a", "a", "b"]
    return_dict: dict[str, int] = {
        'h': 1,
        'a': 2,
        'b': 1
    }
    assert count(str_list) == return_dict


def test_count_use_case_01() -> None:
    """Test."""
    str_list: list[str] = ["h", "a", "a", "a"]
    return_dict: dict[str, int] = {
        'h': 1,
        'a': 3
    }
    assert count(str_list) == return_dict


def test_count_empty() -> None:
    """Test."""
    str_list: list[str] = []
    return_dict: dict[str, int] = dict()
    assert count(str_list) == return_dict
