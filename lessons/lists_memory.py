"""x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0"""


def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1


msg: list[int] = [4, 5, 6]
lessen(msg)
