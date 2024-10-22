"""Finding the maximum # in a list and removing it!"""

__author__ = "730732196"


def find_and_remove_max(input: list[int]) -> int:
    if not input:
        return -1
    max_value = input[0]
    for elem in input:
        if elem > max_value:
            max_value = elem
    index: int = 0
    while index < len(input):
        if input[index] == max_value:
            input.pop(index)
        else:
            index += 1
    return max_value
