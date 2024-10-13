"""Mutating functions."""

__author__ = "730732196"


def manual_append(a: list[int], number: int) -> None:
    a.append(number)


def double(a: list[int]) -> None:
    index: int = 0
    while index < len(a):
        a[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
