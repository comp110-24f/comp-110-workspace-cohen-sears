"""My first Challenge Question!"""

__author__ = "730732196"


def mimic(message: str) -> str:
    """Mimic a message"""
    return message


def main() -> None:
    """Pulls together the functions"""
    # print(mimic(message="Howdy!"))
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
