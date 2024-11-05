import random

# Variables
player_throw = []
comp_throw = []
player_stats = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "three_of_a_kind":0,
    "four_of_a_kind":0,
    "full_house":0,
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

def throw_dice():
    return random.randrange(1, 7)

def throw(n = 5):
    values = []
    for i in range(1, n+1):
        outcome = throw_dice()
        values.append(outcome)
    return values

def player_turn():
    # Print current stats
    current_stats = []

    for entry in player_stats.values():
        current_stats.append(entry)
    
    print(f"Current scores:\n"
          f"{"Ones:":<20}{current_stats[0]:<10}\n"
          f"{"Twos:":<20}{current_stats[0]:<10}\n"
          f"{"Threes:":<20}{current_stats[0]:<10}\n"
          f"{"Fours:":<20}{current_stats[0]:<10}\n"
          f"{"Fives:":<20}{current_stats[0]:<10}\n"
          f"{"Sixes:":<20}{current_stats[0]:<10}\n"
          f"{"Three of a kind:":<20}{current_stats[0]:<10}\n"
          f"{"Four of a kind:":<20}{current_stats[0]:<10}\n"
          f"{"Full house:":<20}{current_stats[0]:<10}\n"
          f"{"Small street:":<20}{current_stats[0]:<10}\n"
          f"{"Large street:":<20}{current_stats[0]:<10}\n"
          f"{"Yahtzee:":<20}{current_stats[0]:<10}\n"
          f"{"Chance:":<20}{current_stats[0]:<10}\n")
    
    # first turn
    score = throw()
    print(f"Your throw: {score}")

    # Determine which score types can be saved


    # Player chooses option
    player_choice = input(f"What do you want to do?")
    
    # second turn

    # third turn


def play():
    while True:
        player_turn()

if __name__ == "__main__":
    play()