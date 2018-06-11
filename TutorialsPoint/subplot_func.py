import numpy as np
import matplotlib.pyplot as plt


# plotting both sine and cosine values
# compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
print(x)
y_sin = np.sin(x)
print(y_sin)
y_cos = np.cos(x)
# set up a subplot grid that has height 2 and width 1, and set the first such subplot as active
plt.subplot(2, 1, 1)
# make the first plot
plt.plot(x, y_sin)
plt.title("Sine")
# set the second subplot as active, and make the second plot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("Cosine")
# show the figure
plt.show()
