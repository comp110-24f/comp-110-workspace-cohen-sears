"""Dictionary Utility Functions!"""

__author__ = "730732196"


def invert(dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key in dict:
        value = dict[key]
        # Every key needs to be looped through
        if value in inverted_dict:
            raise KeyError(f"Duplicate value found for '{key}'.")
        # I think this error is good enough and accurately sums up the situation
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(dict: dict[str, str]) -> str:
    color_count = {}
    # Dict needed to count the number of times color appears
    for name in dict:
        color = dict[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        # If there is a tie, it keeps the color that appears first
    most_popular = ""
    # Needs to be defined as an empty string, so it can be returned even if empty
    max_count = 0
    for name in dict:
        color = dict[name]
        if color_count[color] > max_count:
            most_popular = color
            max_count = color_count[color]
        elif color_count[color] == max_count and most_popular is None:
            most_popular = color
    return most_popular


# Split up into basic parts and diagram if needed to help complexity


# Next time go to office hours earlier so this makes more sense (Mental Note)


def count(items: list[str]) -> dict[str, int]:
    dict = {}
    for elem in items:
        if elem in dict:
            dict[elem] += 1
        # Increase if already present in list
        else:
            dict[elem] = 1
        # Needed for new keys
    return dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    dict = {}
    for word in words:
        first_letter = word[0].lower()
        # Given in directions
        # Retrieves the first letter in lowercase (makes things easier)
        if first_letter in dict:
            dict[first_letter].append(word)
        else:
            dict[first_letter] = [word]
    return dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    # Slightly confused on the returning none, but example returns the function
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
    # Wouldnt a print statement have to be used to aquire this?
