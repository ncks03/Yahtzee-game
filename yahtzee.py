import random

# Variables
player_throw = []
comp_throw = []
player_stats = {}
computer_stats = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "three_of_a_kind":0,
    "four_of_a_kind":0,
    "small_street":0,
    "large_street":0,
    "yahtzee":0,
    "chance":0,
}
player_totals = {
    "top":0,
    "bonus":0,
    "bottom":0,
    "total":0
}
computer_totals = {
    "top":0,
    "bonus":0,
    "bottom":0,
    "total":0
}
is_player_turn = True

def throw_dice():
    return random.randrange(1, 7)

def throw(n = 5):
    values = []
    for i in range(1, n+1):
        outcome = throw_dice()
        values.append(outcome)
    return values

def player_turn():
    # Throw dices
    score = throw()
    print(f"Your throw: {score}")

    # Determine which score types can be saved

    # Player chooses option
    player_choice = input(f"What do you want to do?")
    
    # Throw remaining dices


def play():
    while True:
        if is_player_turn:
            player_turn()

if __name__ == "__main__":
    play()