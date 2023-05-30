import matplotlib.pyplot as plt
from graph_functions import squares

plt.style.use('seaborn')
fig, ax = plt.subplots()

# Get input and outputs values calling squares function from mpl_squares file
values = squares(1,1001)
input = values[0]
output = values[1]

# Using colormaps
ax.scatter(input,output, c=output, cmap=plt.cm.flag , s=10)

# Set char title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of the tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

# Saving plots automatically
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()


