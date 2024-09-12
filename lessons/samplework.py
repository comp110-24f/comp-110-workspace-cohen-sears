def check_first_letter(word: str, letter: str) -> str:
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
