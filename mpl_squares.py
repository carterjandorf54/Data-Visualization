import matplotlib.pyplot as plt
from graph_functions import squares

values = squares(3,10)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(values[0], values[1], linewidth=3)

# Set Chart title and Label Axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=24)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()