"""Practice with Condtionals, Local Variables, and User Input"""

__author__ = "730732196"


def guess_a_number() -> None:
    """Inputs will be made by user"""
    secret: int = 7
    # Convert input to int for comp with the secret number
    guess = int(input("Guess a number:"))
    # Printing the guess back to the user
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < 7:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")


# Calling the function (more info on structure later)
if __name__ == "__main__":
    guess_a_number()
