import matplotlib.pyplot as plt
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for _ in range(5000)]

frequencies = [results.count(value) for value in range(2, 13)]

plt.style.use("classic")
fig, ax = plt.subplots()
ax.bar(range(2, 13), frequencies)

ax.set_title("Matplotlib: Rolling Two D6 Dice")
ax.set_xlabel("Result")
ax.set_ylabel("Frequency")

plt.show()
