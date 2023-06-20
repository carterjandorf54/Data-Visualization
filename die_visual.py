# Testing out updating a branch in the remote repository

from die import Die
import plotly.express as px

# Create a list of die
die = Die()
die_2 = Die(10)
# die_3 = Die()
die_list = [die, die_2]
# Create a results list
results = []

# Create a loop to roll the die
num_rolls = 50000
for roll_num in range(num_rolls):
    result = sum([x.roll() for x in die_list])
    results.append(result)

# Analyze the results
frequencies = []
max_result = sum([x.num_sides for x in die_list])
poss_results = range(2, max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = f"Results of Rolling One D{die.num_sides} and One D{die_2.num_sides} {num_rolls} Times"
labels = {'x': "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further Customize the Chart
fig.update_layout(xaxis_dtick=1)

# Write to an HTML File
fig.write_html(f'dice_visual_d6{die.num_sides}d{die_2.num_sides}.html')


fig.show()
