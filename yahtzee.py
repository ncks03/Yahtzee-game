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
    "small_straight":0,
    "large_straight":0,
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
    """
    Generates a total of n random numbers (default 5).
    """
    values = []
    for i in range(1, n+1):
        outcome = throw_dice()
        values.append(outcome)
    return values

def player_turn():
    """
    Plays 3 turns and lets the player choose which scores to keep.
    """
    # Print current stats
    current_stats = []
    turn_score = 0

    # Append current stats to list
    for entry in player_stats.values():
        if entry == 0:
            current_stats.append("")
        elif entry == None:
            current_stats.append("-")
        else:
            current_stats.append(entry)
    
    print(f"Current scores:\n"
          f"{"Ones:":<20}|{current_stats[0]:<2}|\n"
          f"{"Twos:":<20}|{current_stats[1]:<2}|\n"
          f"{"Threes:":<20}|{current_stats[2]:<2}|\n"
          f"{"Fours:":<20}|{current_stats[3]:<2}|\n"
          f"{"Fives:":<20}|{current_stats[4]:<2}|\n"
          f"{"Sixes:":<20}|{current_stats[5]:<2}|\n"
          f"{"Three of a kind:":<20}|{current_stats[6]:<2}|\n"
          f"{"Four of a kind:":<20}|{current_stats[7]:<2}|\n"
          f"{"Full house:":<20}|{current_stats[8]:<2}|\n"
          f"{"Small straight:":<20}|{current_stats[9]:<2}|\n"
          f"{"Large straight:":<20}|{current_stats[10]:<2}|\n"
          f"{"Yahtzee:":<20}|{current_stats[11]:<2}|\n"
          f"{"Chance:":<20}|{current_stats[12]:<2}|\n")
    
    # first turn
    score = throw()
    print(f"Your throw: {score}")

    # Determine which score types can be saved
    possible_options = set()

    for number in score:
        possible_options.add(str(number))
        if 
    
    # Player chooses option
    print(f"You can choose from: {", ".join(possible_options)}")
    player_choice = input(f"What do you want to do? ")

    if str(player_choice) in possible_options:
        if int(player_choice) in range(1, 7):
            for number in score:
                if number == int(player_choice):
                    turn_score += number
                else:
                    continue
        else:
            print("Invalid choice")
    else:
        print("An error occured")
                
    player_stats[str(player_choice)] = turn_score

    print(player_stats)


def play():
    while True:
        player_turn()

if __name__ == "__main__":
    play()