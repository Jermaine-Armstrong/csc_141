from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """A class representing a single die."""
    def __init__(self, sides=8):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die_1 = Die(8)
die_2 = Die(8)

rolls = 1000
results = [die_1.roll() + die_2.roll() for _ in range(rolls)]

min_result = 2        # 1+1
max_result = 16       # 8+8
frequencies = [results.count(value) for value in range(min_result, max_result + 1)]

x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

layout = Layout(
    title=f"Results of Rolling Two D8 Dice {rolls:,} Times",
    xaxis={"title": "Result"},
    yaxis={"title": "Frequency"},
)

offline.plot({"data": data, "layout": layout},
             filename="two_d8s_visual.html")
