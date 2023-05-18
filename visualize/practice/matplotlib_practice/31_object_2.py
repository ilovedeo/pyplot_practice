import matplotlib.pyplot as plt
import numpy as np

# https://wikidocs.net/141562

###
# Usage example.
x = np.arange(1, 5) # [1, 2, 3, 4]

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
ax[0][0].plot(x, np.sqrt(x))
ax[0][1].plot(x, x)
ax[1][0].plot(x, -x+5)
ax[1][1].plot(x, np.sqrt(-x+5))

plt.show()

###
# Set style;
x = np.arange(1, 5)
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True, squeeze=True)

# (0, 0) plot;
ax[0][0].plot(x, np.sqrt(x), linestyle="-", color="gray", linewidth=3, label="root")
ax[0][0].legend()

# (0, 1) plot;
ax[0][1].plot(x, x, linestyle="-", color="green", marker="^", markersize="10", label="y=x")
ax[0][1].legend()

# (1, 0) plot;
ax[1][0].plot(x, -x+5, linestyle="--", color="red", marker="o", label="y=-x+5")
ax[1][0].legend()

# (1, 1) plot;
ax[1][1].plot(x, np.sqrt(-x+5), linestyle="-.", color="blue", marker="o", label="y=np.sqrt(-x+5)")
ax[1][1].legend()

plt.show()
