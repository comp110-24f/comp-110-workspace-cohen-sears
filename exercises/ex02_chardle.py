"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730732196"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        # Could use a while loop to repeat, but not permitted in this assignment
        return word
    else:
        print("Error: Word must contain 5 characters.")
    exit()


# The exit function must be used after the error so that the input_word restarts


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    # Remember: print and return do not have the same functionality
    else:
        print("Error: Character must be a single character.")
    exit()


# The exit function must be used after the error so that the input_word restarts


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # Used to count the number of matching letters
    if letter == word[0]:
        print(letter + " found at index 0")
        count += 1
    # Each time a match is found anywhere, incerease the count variable by 1
    # Continue repeating throughout the entirety of each word
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1
    # The index only goes to [4] since the word is 5 letters!
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    # elif used instead of if + else
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# Necessary for calling the functions

if __name__ == "__main__":
    main()
