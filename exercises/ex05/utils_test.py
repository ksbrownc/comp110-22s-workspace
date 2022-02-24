"""Ex05 - 'List' Utility Functions."""

__author__ = "730327035"

from utils import only_evens, sub, concat


def test_only_evens_use_case() -> None:
    """Tests for the only_evens function with odd integers."""
    only: list[int] = [9, 13, 15, 19]
    assert only_evens(only) == []


def test_only_evens_use_case_part_two() -> None:
    """Tests for the only_evens function with even integers."""
    only: list[int] = [4, 10, 16, 19]
    assert only_evens(only) == [4, 10, 16]


def test_only_evens_theedge_case() -> None:
    """Testing for the only_evens function edge case."""
    only: list[int] = []
    assert only_evens(only) == []


def test_sub_use_case() -> None:
    """Tests for the sub function."""
    some_list: list[int] = [18, 29, 56, 84, 99]
    begin: int = 1
    finale: int = 3
    assert sub(some_list, begin, finale) == [29, 56]


def test_sub_use_case_partwo() -> None:
    """Tests for the sub function."""
    some_list: list[int] = [18, 29, 56, 84, 99]
    begin: int = 0
    finale: int = 4
    assert sub(some_list, begin, finale) == [18, 29, 56, 84]


def test_sub_use_thedgecase() -> None:
    """Tests for the sub function."""
    some_list: list[int] = [18, 29, 56, 94, 99]
    begin: int = -1
    finale: int = 6
    assert sub(some_list, begin, finale) == [18, 29, 56, 94, 99]


def test_concat_use_case() -> None:
    """Tests for the concat function."""
    con: list[int] = [8, 10, 12]
    cat: list[int] = [6, 7, 9]
    assert concat(con, cat) == [8, 10, 12, 6, 7, 9]


def test_concat_use_case_parttwo() -> None:
    """Tests for the concat function."""
    con: list[int] = [3, 4, 5]
    cat: list[int] = [6, 7, 9]
    assert concat(con, cat) == [3, 4, 5, 6, 7, 9]


def test_concat_theedgecase() -> None:
    """Tests for the concat function."""
    con: list[int] = []
    cat: list[int] = []
    assert concat(con, cat) == []
