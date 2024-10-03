"""Concatentation of two input strings!"""

__author__ = "730732196"


def concat(string1: str, string2: str) -> str:
    return str(string1) + str(string2)


word1: str = "happy"
word2: str = "tuesday"


if __name__ == "__main__":
    print(concat(word1, word2))
