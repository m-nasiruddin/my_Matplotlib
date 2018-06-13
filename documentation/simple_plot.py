import matplotlib.pyplot as plt
import numpy as np


# data for plotting
t = np.arange(0.0, 2.0, 0.01)
print(t)
s = 1 + np.sin(2 * np.pi * t)
print(s)
# note that using plt.subplots below is equivalent to using fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
ax.grid()
fig.savefig("output/test.png")
plt.show()
