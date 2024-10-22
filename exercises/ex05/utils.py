"""Implementation of list utility functions!"""

__author__ = "730732196"


def only_evens(a: list[int]) -> list[int]:
    even_list = []
    # An empty list is necessary to start appending the elements to
    for elem in a:  # Use for loop over while loop all day, much less confusing
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


# Makes sure to remeber important topics like modulo (dont get stuck next time)


def sub(b: list[int], start_index: int, end_index: int) -> list[int]:
    if len(b) == 0 or start_index >= len(b) or end_index <= 0:
        return []
    # If list is empty, start is out of bounds, or end is less than 0,
    # then an empty list is needed
    if start_index < 0:
        start_index = 0
    # Defaulting negatives to start at the beginning
    if end_index > len(b):
        end_index = len(b)
    # Adjusts to the length of the list
    final_list = []
    for elem in range(start_index, end_index):
        final_list.append(b[elem])
    # Slice notation has not been learned/permitted so looping is the proper way
    return final_list


def add_at_index(c: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(c):
        raise IndexError("Index is out of bounds for the input list")
    # The index error was given, however it is important to know the raise function
    c.append(0)
    # Placeholder for another element in the list (could use anything)
    for elem in range(len(c) - 1, index, -1):
        c[elem] = c[elem - 1]
    # Shifts all the elements to the right starting from the end of the list up
    # to the specified index
    c[index] = element
