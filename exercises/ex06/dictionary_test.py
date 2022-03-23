
"""Tests for EX06 Functions."""


__author__ = "730319713"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count

import pytest


def test_invert_blanks() -> None:
    """Edge case for blank str."""
    assert invert({' ': 'w', 'x': ' '}) == {'w': ' ', ' ': 'x'}


def test_invert_abcxyz() -> None:
    """Use case 1 for invert fn."""
    assert invert({'a': 'x', 'b': 'y', 'c': 'z'}) == {'x': 'a', 'y': 'b', 'z': 'c'}


def test_invert_af() -> None:
    """Use case 2 for invert fn."""
    assert invert({'a': 'f'}) == {'f': 'a'}


def test_favorite_color_first() -> None:
    """Edge case for first color in dict."""
    assert favorite_color({'Eli': 'red', 'Elly': 'green', 'Elias': 'red', 'Emi': 'green'}) == "red"


def test_favorite_color_u1() -> None:
    """Usage case for favorite color fn."""
    assert favorite_color({'Eli': 'blue', 'Elly': 'green', 'Elias': 'red', 'Emi': 'green'}) == "green"


def test_favorite_color_u2() -> None:
    """Usage case 2 for favorite color fn."""
    assert favorite_color({'Jonny': 'blue', 'Joan': 'grey', 'Joel': 'grey', 'Joe': 'grey'}) == "grey"


def test_count_empty() -> None:
    """Edge case for empty list."""
    alist: list[str] = list()
    assert count(alist) == {}


def test_count_u1() -> None:
    """Usage case 1 for count fn."""
    blist: list[str] = ["hat", "car", "wheel", "hat", "cap", "hat"] 
    assert count(blist) == {"hat": 3, "car": 1, "wheel": 1, "cap": 1}


def test_count_u2() -> None:
    """Usage case 2 for count fn."""
    clist: list[str] = ["hat", "car", "car", "car", "car", "cap", "cap", "cap", "cap", "cap"] 
    assert count(clist) == {"hat": 1, "car": 4, "cap": 5}


def test_keyerror() -> None:
    """Keyerror test."""
    with pytest.raises(KeyError):
        thedict = {'jon': 'athan', 'n': 'athan'}
        invert(thedict)