import random

player_score = []
is_running = True

def throw_dice():
    return random.randrange(1, 7)

def throw(n = 5):
    """
    Generates a total of n random numbers (default 5).
    """
    values = []
    for i in range(1, n+1):
        outcome = throw_dice()
        values.append(outcome)
    return values

def turn_1():
    # generate 5 values
    values = throw()
    print(f"1st throw: {''.join(str(values))}")

    # ask which values to save
    saved_values = []
    saving_values = True
    while saving_values:
        choice = input("What value do you want to save? (number 1-5, type 'save' to save values) ")
        if choice.lower() == "save":
            saving_values = False
        else:
            saved_values.append(values[int(choice)-1])

    # return saved values
    return saved_values

def turn_2(saved_values: list):
    # generate n values based on number of saved values
    amount = 5 - len(saved_values)
    values = throw(amount)
    print(f"2nd throw: {''.join(str(values))}")

    # ask which values to save
    saving_values = True
    while saving_values:
        choice = input(f"What value do you want to save? (number 1-{amount}, type 'save' to save values) ")
        if choice.lower() == "save":
            saving_values = False
        else:
            saved_values.append(values[int(choice)-1])

    # return saved values
    return saved_values

def turn_3(saved_values: list):
    # generate n values based on number of saved values
    amount = 5 - len(saved_values)
    values = throw(amount)
    print(f"3rd throw: {''.join(str(values))}")

    # ask which values to save
    saving_values = True
    while saving_values:
        choice = input(f"What value do you want to save? (number 1-{amount}, type 'save' to save values) ")
        if choice.lower() == "save":
            saving_values = False
        else:
            saved_values.append(values[int(choice)-1])

    # return saved values
    return saved_values

def save_score(values: list):
    # Determine which score types can be saved
    possible_options = set()

    for number in values:
        possible_options.add(str(number))
        if values.count(number) == 3:
            possible_options.add("3 of a kind")
        elif values.count(number) == 4:
            possible_options.add("4 of a kind")
        elif values.count(number) == 5:
            possible_options.add("yahtzee")

    option_choices = enumerate(possible_options, start=1)
    print(option_choices)

    for index, option in option_choices:
        print(f"{index}: {option}")

    choice = input("What do you want to save?")



def print_score():
    pass

round = 1

while is_running:
    # Print round header
    print("-"*50)
    print(f"Round {round}")
    print("-"*50)

    # Play 3 turns and save score
    print_score()
    score = turn_1()
    score = turn_2(score)
    score = turn_3(score)
    save_score(score)

    # Increase round by 1
    round += 1