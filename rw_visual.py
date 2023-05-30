import matplotlib.pyplot as plt
import math
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use('classic')

# Call the subplots method and declare a figure size
fig, ax = plt.subplots(figsize=(16, 9), dpi=81.59)

# Point Numbers creates a range from 0 to the number of points, this is for use in the scatter call
point_numbers = range(rw.num_points)

# Call scatter plot with the x,y values and use point numbers as the color map ranges so we go from light to dark
ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
           cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.set_aspect('equal')
# ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Calculate Distance Walked
total_dis = math.sqrt(
    (rw.x_values[-1] - rw.x_values[0]) ** 2 + (rw.y_values[-1] - rw.y_values[0]) ** 2)
print(f"Distance Traveled = {total_dis}")

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()
