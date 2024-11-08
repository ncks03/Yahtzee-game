import random

score_table = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "3_of_a_kind": 0,
    "4_of_a_kind": 0,
    "full_house": 0,
    "small_straight": 0,
    "large_straight": 0,
    "yahtzee": 0,
    "chance": 0
}

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

def save_values(save_in: int, save_out: list): 
    saving_values = True
    print("What values do you want to save?")
    while saving_values:
        print(f"Your saved values: {''.join(str(save_out))}")
        choice = input("Type the value number (1-5), type 'save' to save values: ")
        if choice.lower() == "save":
            saving_values = False
        else:
            save_out.append(save_in[int(choice)-1])
    return save_out

def turn_1():
    # generate 5 values
    values = throw()
    print(f"1st throw: {''.join(str(values))}")

    # ask which values to save
    saved_values = []
    save_values(values, saved_values)

    # return saved values
    return saved_values

def turn_2(saved_values: list):
    # generate n values based on number of saved values
    amount = 5 - len(saved_values)
    values = throw(amount)
    print(f"2nd throw: {''.join(str(values))}")

    # ask which values to save
    save_values(values, saved_values)

    # return saved values
    return saved_values

def turn_3(saved_values: list):
    # generate n values based on number of saved values
    amount = 5 - len(saved_values)
    values = throw(amount)
    print(f"3rd throw: {''.join(str(values))}")

    # ask which values to save
    save_values(values, saved_values)

    # return saved values
    return saved_values

def save_choice(values: list):
    # Determine which score types can be saved
    possible_options = []

    for number in values:
        if number not in possible_options:
            possible_options.append(str(number))
        
        if values.count(number) == 3:
            possible_options.append("3_of_a_kind")
        elif values.count(number) == 4:
            possible_options.append("4_of_a_kind")
        elif values.count(number) == 5:
            possible_options.append("yahtzee")

    for option in possible_options:
        if score_table[option] != 0:
            possible_options.remove(option)
        else:
            continue
    
    option_choices = enumerate(possible_options, start=1)
    print(option_choices)

    for index, option in option_choices:
        print(f"{index}: {option}")

    choice = int(input(f"What do you want to save? (1-{len(possible_options)})"))

    save_choice = possible_options[choice-1]

    return save_choice

def save_score(values, save_action):
    if save_action == "1" or "2" or "3" or "4" or "5" or "6":
        total_score = values.count(int(save_action)) * int(save_action)
    elif save_action == "3_of_a_kind" or "4_of_a_kind" or "yahtzee" or "chance":
        total_score == sum(values, start=0)
    elif save_action == "full_house":
        total_score = 25
    elif save_action == "small_straight":
        total_score = 30
    elif save_action == "large_straight":
        total_score = 40
    else:
        print("No valid action found")
        return None
    
    score_table[save_action] = total_score

def print_score():
    print(score_table)

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
    end_score = turn_3(score)
    save_action = save_choice(end_score)
    save_score(end_score, save_action)
    print_score()

    # Increase round by 1
    round += 1