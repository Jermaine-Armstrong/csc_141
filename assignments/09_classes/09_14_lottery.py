import random

lottery_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'A', 'B', 'C', 'D', 'E']

winning_number = random.sample(lottery_numbers, 4)
print("Winning Lottery Numbers:", winning_number)
