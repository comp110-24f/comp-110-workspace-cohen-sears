"""EX04 - Listing Utility Functions"""

__author__ = "730732196"


def all(vals: list[int], num: int) -> bool:
    if not vals:  # Could have used a length checker, but not needed
        return False  # This has to be here in order to check an empty list
    for elem in vals:
        if elem != num:
            return False  # Loops through all the numbers
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # This was given from the instructions
    # Remeber this notation for future assignments
    max_value = input[0]
    # Making sure the max is assigned to the first num in the list
    for elem in input:
        if elem > max_value:
            max_value = elem
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False  # We can not assume the lengths are equal
    for elem in range(len(list1)):
        if list1[elem] != list2[elem]:
            return False
        # Both lists need to be compared at every index/elem
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:
        list1.append(elem)


# Avoid getting confused next time on the append function
# For this example, we append the list2 to list1

# Could have a main function but I felt it wasn't needed
