import matplotlib.pyplot as plt
import numpy as np

# Define the x and y values for the original data
x_values = [7,8,9,10,11,12,13,14,15,16,17,18]
y_values = [28.88602, 47.42578, 78.64864, 129.18977, 216.73497, 361.42056, 602.32530, 1009.19913, 1689.24427, 2828.77767, 4740.25243, 7949.60410]


x_line = np.arange(7, 19)
y_line = 28.88602 * np.power(1.666325674, (x_line - 7))

# Create the plot and set the x and y labels
fig, ax = plt.subplots()
ax.plot(x_values, y_values, marker='o', label='Data')
ax.plot(x_line, y_line, label='f(n)')
ax.set_xlabel('2^X vertices')
ax.set_ylabel('MST Weight')

# Set the plot title

ax.set_title('Average MST weight vs Number of Vertices(d = 4)')

# Show the legend
ax.legend()

# Show the plot
plt.show()
