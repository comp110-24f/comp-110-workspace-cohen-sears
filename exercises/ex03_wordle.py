"""EX03 - Wordle - The actual game!"""

__author__ = "730732196"


def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len} character word: ")
    # This line of code should not be placed in the while loop
    # This way, the input is not asked every time unless False
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # The input needs to be accessed after the "Try again:" not a new line
    return guess


# Spend less time trying to make the code more complicated than it needs to


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks to see if the letter guess is in the secret word!"""
    assert len(char_guess) == 1  # This ensures the argument is one character
    # Remember this important assert statement for later code!
    index = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


# True is the letter is present, false if not


def emojified(guess: str, secret: str) -> str:
    """Given a guess and secet word --> emojify the results"""
    assert len(guess) == len(secret)  # Guess and secret need to be same length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # The named constants above do not need to be memorized
    # However, know the basics of how they are structured
    answer: str = ""
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            answer += GREEN_BOX
        elif contains_char(secret, guess[index]):
            # Call to contains_char to go through and check each letter
            answer += YELLOW_BOX
        else:
            answer += WHITE_BOX
        # Assigning of emojis to each character
        index += 1
    return answer


# Output should show list of emojis in response to guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = 6  # Changed from turn_number (makes more sense)
    turn_count: int = 0
    win: bool = False
    while turn_count < max_turns and not win:
        # if one is false the while loop is exited
        turn_count += 1
        print(f"=== Turn {turn_count}/6 ===")
        guess = input_guess(len(secret))  # Call to earlier function
        answer = emojified(guess, secret)  # Call to earlier function
        print(answer)

        if guess == secret:  # Do not need an else here
            win = True
    # Helps to exit the while loop and enters the next conditional

    if win:
        print(f"You won in {turn_count}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    # Changed from inside the above if in the while loop to outside


if __name__ == "__main__":
    main(secret="codes")
