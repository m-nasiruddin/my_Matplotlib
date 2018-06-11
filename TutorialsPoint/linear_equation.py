import numpy as np
from matplotlib import pyplot as plt


# script for plotting the equation (linear) y=2x+5
x = np.arange(1, 11)  # this function creates an ndarray object x as the values on the x axis
print(x)
y = 2 * x + 5  # another ndarray object y as the values on the y axis
print(y)
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)  # values are plotted using this function
plt.show()  # the graphical representation id displayed by this function

plt.plot(x, y, "ob")  # displays the circles representing points in blue color, instead of the line in blue color
plt.show()
