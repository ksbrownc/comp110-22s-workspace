"""EX06 - Dictionary Functions ."""

__author__ = "730327035"

from dictionary import invert, favorite_color, count 
import pytest


def test_invert_usecase() -> None:
    """Tests for invert function that re-arranges the value and keys."""
    z: dict[str, str] = {'Kayla': 'Brown', 'Journey': 'Fields'}
    assert invert(z) == {'Brown': 'Kayla', 'Fields': 'Journey'}


def test_invert_usecase2() -> None:
    """Tests for invert function that re-arranges the value and the keys, but if there is a key error."""
    with pytest.raises(KeyError):
        invert({'Kayla': 'Brown', 'Journey': 'Brown'})


def test_invert_edgecase() -> None:
    """Tests for invert function in edge case."""
    z: dict[str, str] = {}
    assert invert(z) == {}


def test_favorite_color_usecase() -> None:
    """Tests for the favorite_color function for favorite colors."""
    namescolor: dict[str, str] = {'Kyle': 'Blue', 'Sam': 'Red', 'Dre': 'Pink'}
    assert favorite_color(namescolor)


def test_favorite_color_usecase2() -> None:
    """Tests for the favorite_color function for favorite colors if there is a popular one."""
    namescolor: dict[str, str] = {'Kyle': 'Blue', 'Sam': 'Blue', 'Dre': 'Pink'}
    assert favorite_color(namescolor) == 'Blue'


def test_favorite_color_edgecase() -> None:
    """Tests for the favorite_color function amongst people."""
    namescolor: dict[str, str] = {}
    assert favorite_color(namescolor) == ""


def test_count_usecase() -> None:
    """Tests for the count function for how many times value appears."""
    a: list[str] = ['one', 'two', 'three']
    empty: dict[str, int] = {'one': 1, 'two': 1, 'three': 1}
    assert count(a) == empty


def test_count_usecase2() -> None:
    """Tests for the count function."""
    a: list[str] = ['one', 'two', 'two']
    empty: dict[str, int] = {'one': 1, 'two': 2}
    assert count(a) == empty


def test_count_edgecase() -> None:
    """Tests for the count function."""
    a: list[str] = []
    empty: dict[str, int] = {}
    assert count(a) == empty