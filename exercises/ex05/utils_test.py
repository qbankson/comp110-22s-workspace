"""Test List Utility Functions."""

__author__ = "730319713"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens() -> None:
    assert only_evens([1, 2, 3]) == [2]
    samenum_list: list[int] = [4, 4, 4]
    assert only_evens(samenum_list) == [4, 4, 4]


def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 0, 3) 


def test_concat() -> None:
    xlist: list[int] = [1, 2, 3, 4]
    ylist: list[int] = [7, 9, 11]
    assert concat(xlist, ylist) 