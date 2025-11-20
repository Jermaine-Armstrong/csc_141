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

results = [die_1.roll() * die_2.roll() for _ in range(50_000)]

min_result = 1
max_result = 36
frequencies = [results.count(value) for value in range(min_result, max_result+1)]

x_values = list(range(min_result, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

layout = Layout(
    title="Multiplying the Results of Two D6 Dice (50,000 rolls)",
    xaxis={"title": "Product"},
    yaxis={"title": "Frequency"},
)

offline.plot({"data": data, "layout": layout}, filename="15-8_multiplication.html")
