"""Practice with unit tests for find_max!"""

__author__ = "730732196"

from CQs.cq07.find_max import find_and_remove_max


def test_returns_max_value_use_case() -> None:
    a: list[int] = [3, 5, 7, 2, 7, 4]
    assert find_and_remove_max(a) == 7


def test_mutates_input_list_use_case() -> None:
    a: list[int] = [3, 5, 7, 2, 7, 4]
    find_and_remove_max(a)
    assert a == [3, 5, 2, 4]


def test_empty_list_edge_case() -> None:
    a: list[int] = []
    assert find_and_remove_max(a) == -1
    assert a == []
