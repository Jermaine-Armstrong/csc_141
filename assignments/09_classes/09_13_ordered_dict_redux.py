import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(die.roll(), end=' ')