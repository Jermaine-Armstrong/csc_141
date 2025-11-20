from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die = Die()

results = [die.roll() for _ in range(10)]

frequencies = [results.count(value) for value in range(1, die.sides + 1)]

print("Results:", results)
print("Frequencies:", frequencies)
