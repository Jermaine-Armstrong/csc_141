from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(50_000)]

min_result = 3
max_result = 18
frequencies = [results.count(value) for value in range(min_result, max_result+1)]

x_values = list(range(min_result, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

layout = Layout(
    title="Results of Rolling Three D6 Dice (50,000 rolls)",
    xaxis={"title": "Result"},
    yaxis={"title": "Frequency"},
)

offline.plot({"data": data, "layout": layout}, filename="15-7_three_d6.html")
