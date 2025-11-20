import random

lottery_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'A', 'B', 'C', 'D', 'E']

my_ticket = random.sample(lottery_numbers, 4)

attempts = 0
winning_number = []

while True:
    if my_ticket == winning_number:
        break
    winning_number = random.sample(lottery_numbers, 4)
    attempts += 1

print(f"My Lottery Ticket: {my_ticket}")
print(f"Winning Lottery Numbers: {winning_number}")
print(f"Number of attempts to win: {attempts}")