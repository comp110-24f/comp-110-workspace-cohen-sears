def get_first(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    return input[0]


def remove_first(input: list[int]) -> None:
    if len(input) > 0:
        input.pop(0)


def remove_and_get_first(input: list[int]) -> int:
    first: int = input[0]
    input.pop(0)
    return first  # input[0]
