import numpy as np
import matplotlib.pyplot as plt


# compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
print(x)
y = np.sin(x)
print(y)
plt.title("sine wave form")

# plot the points using Matplotlib
plt.plot(x, y)
plt.show()
