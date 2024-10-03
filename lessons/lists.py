"Practice using lists"

# my_numbers: list[float] = list()

# my_numbers.append(1.5)

# print(my_numbers)


game_points: list[int] = [102, 86, 94, 94]

print(game_points)

# last_game: int = game_points[2]
# print(last_game)

print(game_points[2])

game_points[1] = 72

print(game_points)

# Strings are not mutable; therefore no replacement!

# Length of gamepoints

print(len(game_points))

# Removing 72
game_points.pop(1)

print(game_points)


# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points


def display(Input: list[int]) -> None:
    index: int = 0
    while index < len(game_points):
        print(Input[index])
        index += 1
    return None


display(Input=game_points)

print(game_points[10])
