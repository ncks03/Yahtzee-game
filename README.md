# Yahtzee-game

This is an application where you can play the single player dice game Yahtzee!

# The game

The purpose of the game is to get the highest score. Each turn you get 3 throws. Each throw you throw 5 dices and can choose which dices you want to keep. Then you throw the remaining dices. After the 3rd throw you can choose where you want to put your score:

| Field | Points | Requires |
|---|---|---|
| Numbers (1-6) | All instances of the number added together | At least 1 instance of the number |
| 3 of a kind | Total of all values | 3 or more of the same number |
| 4 of a kind | Total of all values | 4 or more of the same number |
| Full house | 25 | 3 of one number and 2 of another |
| Small straight | 30 | 4 consecutive numbers (1-4, 2-5 or 3-6) |
| Large straight | 40 | 5 consecutive numbers (1-5 or 2-6) |
| Yahtzee | First time 50, then 100 | All 5 values are the same |
| Chance | Total of all values | Can be any combination of values |

Once a score field has been filled, it can't be changed.

When you can't save your score anywhere, you can cross out a field. Crossing out fields blocks this field for the rest of the game, and you won't get points for this field. For example when your final throw is 3, 3, 2, 2, 1 and you already have the ones, twos, threes and chance filled, you have to cross out a field.

The first time you throw Yahtzee, you get 50 points. For every Yahtzee after that, you can add 100 points to the Yahtzee field. Because you effectively skip a turn, you can then also save the values in the corresponding number field (If it isn't filled yet) or in 3 of a kind, 4 of a kind or chance fields. If you don't have a field you can fill you'll have to cross out a field.

# Scoring

Your final score will be counted as follows:
The scores for all number fields are counted. If the total count of the number fields is 63 or more, you get 35 bonus points. Then the rest of the fields will be counted and added on top of the number fields and bonus. This is your final score
