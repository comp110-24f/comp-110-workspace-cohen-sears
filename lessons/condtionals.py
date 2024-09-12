def less_than_10(num: int) -> None:
    """Tell us if num<10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Bg Number")


(less_than_10(num=7))
