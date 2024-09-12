"""Planning a cozy tea party!"""

# number of guests,tea bags,treats and the expected cost of the party.


__author__ = "730732196"


def main_planner(guests: int) -> None:
    """Calls all of the functions and produces printed output"""
    tea_count: int = tea_bags(
        people=guests
    )  # Variables are necessary for the cost function
    treat_count: int = treats(people=guests)
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # Printing strings, recalling specific functions
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_count, treat_count=treat_count)))
    # Next time do not get stuck on using a complicated nested function when I can use
    # variables to assign Tea_count and treat_count to the number of teabags and treats


def tea_bags(people: int) -> int:
    """Tea bag calculation for # of people"""
    return people * 2  # The return value 'people'


# Each person gets 2 tea bags, so multiply the people by 2
# REMEBER TO DIAGRAM OUT WHEN STUCK BECAUSE THAT HELPS A TON (Past self)


def treats(people: int) -> int:
    """Treat calculation based off # of teas"""
    return int(tea_bags(people=people) * 1.5)


# Calculate treats based on 1.5 treats per tea bag
# Tea_bags() returns how many are needed


def cost(tea_count: int, treat_count: int) -> float:
    """Computing the cost of tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


# Total cost: tea bags at 0.50 cents each and treats at 0.75 cents each


#   return (  float((tea_bags(people=tea_count) * 0.50) +
#  tea_bags(people=treat_count) * 0.75)  / 2.0  )
# (This function call also works but is too complex and not necesssary)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# Do not need to know specific function of the "if __name__...", rather understand that
# asks the user how many guests are attending and convert input to an integer that can
# then be actually run
