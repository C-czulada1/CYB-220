import matplotlib.pyplot as plt
from random import randint
from random_walk import RandomWalk
from random import choice
import plotly.express as px
from pathlib import Path
import csv
from datetime import datetime
#15-1
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values)
plt.title("Cube Numbers", fontsize=16)
plt.xlabel("Values", fontsize=12)
plt.ylabel("Cube Numbers", fontsize=12)
plt.show()
#15-2
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s=10)
plt.title("First 5000 Cube Numbers", fontsize=16)
plt.xlabel("Values", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)
plt.show()
#15-3
import matplotlib.pyplot as plt
from random_walk import RandomWalk
rw = RandomWalk(5000)
rw.fill_walk()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_title("Random Walk (Molecular Motion)", fontsize=16)
ax.set_xlabel("X Value", fontsize=12)
ax.set_ylabel("Y Value", fontsize=12)
plt.show()
#15-4
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
#15-5
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step(1)
            y_step = self.get_step(1)
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step
#15-6
results = []
for roll_num in range(1000):
    result = randint(1, 8) + randint(1, 8)
    results.append(result)
frequencies = []
possible_results = range(2, 17)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)
plt.bar(possible_results, frequencies)
plt.title("Results of Rolling Two D8 Dice 1000 Times")
plt.xlabel("Results")
plt.ylabel("Frequency")
plt.show()
#15-7
results = []
for roll_num in range(1000):
    result = randint(1, 6) + randint(1, 6) + randint(1, 6)
    results.append(result)
frequencies = []
possible_results = range(3, 19)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)
plt.bar(possible_results, frequencies)
plt.title("Results of Rolling Three D6 Dice 1000 Times")
plt.xlabel("Results")
plt.ylabel("Frequency")
plt.show()
#15-8
results = []
for roll_num in range(1000):
    result = randint(1, 6) * randint(1, 6)
    results.append(result)
possible_results = sorted(set(results))
frequencies = []
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)
plt.bar(possible_results, frequencies)
plt.title("Results of Multiplying Two D6 Dice")
plt.xlabel("Results")
plt.ylabel("Frequency")
plt.show()
#15-9
results = [randint(1, 6) + randint(1, 6) for _ in range(1000)]
possible_results = range(2, 13)
frequencies = [results.count(value) for value in possible_results]
plt.bar(possible_results, frequencies)
plt.title("Results of Rolling Two D6 Dice")
plt.xlabel("Results")
plt.ylabel("Frequency")
plt.show()
#15-10
x_values = [0]
y_values = [0]
for i in range(1000):
    x_step = choice([-1, 1])
    y_step = choice([-1, 1])
    x_values.append(x_values[-1] + x_step)
    y_values.append(y_values[-1] + y_step)
fig = px.scatter(
    x=x_values,
    y=y_values,
    title="Random Walk (Plotly)"
)
fig.show()
#16-1
path = Path('sitka_weather_2021_full.csv')
lines = path.read_text().splitlines
reader = csv.reader(f)
header_row = next(reader)
dates, precips = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    precip = float(row[5])
    dates.append(current_date)
    precips.append(precip)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, precips, color='blue')
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (in)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()