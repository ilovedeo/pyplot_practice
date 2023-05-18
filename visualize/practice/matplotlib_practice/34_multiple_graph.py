import matplotlib.pyplot as plt
import numpy as np

# Set style;
plt.style.use("default")
plt.rcParams["figure.figsize"] = (4, 3)
plt.rcParams["font.size"] = 5

# Data setting;
x = np.arange(2020, 2027)
y1 = np.array([1, 3, 7, 5, 9, 7, 14])
y2 = np.array([1, 3, 5, 7, 9, 11, 13])

# Draw graphs;
fig, ax1 = plt.subplots()

ax1.plot(
    x,
    y1,
    linestyle="-",
    marker="s",
    color="green",
    markersize=7,
    linewidth=5,
    alpha=0.7,
    label="Price",
)
ax1.set_ylim(0, 18)
ax1.set_xlabel("Year")
ax1.set_ylabel("Price ($)")
ax1.tick_params(axis="both", direction="in")

ax2 = ax1.twinx()
# Width: with of the bar graph;
ax2.bar(x, y2, color="deeppink", alpha=0.7, width=0.7, label="Demand")
ax2.set_ylim(0, 18)
ax2.set_ylabel(r"Demand ($\times10^6$)")
ax2.tick_params(axis="y", direction="in")

ax1.set_zorder(ax2.get_zorder() + 10)
ax1.patch.set_visible(False)  # Set transparent ax1's background;

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.show()
