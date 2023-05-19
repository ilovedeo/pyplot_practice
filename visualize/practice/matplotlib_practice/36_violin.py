import matplotlib.pyplot as plt
import numpy as np

# Set style;
plt.style.use("default")
# plt.rcParams["figure.figsize"] = (4, 3)
plt.rcParams["font.size"] = 10

# Generate data;
np.random.seed(0)
data_a = np.random.normal(0, 2., 1000)
data_b = np.random.normal(-3, 1.5, 500)
data_c = np.random.normal(1.2, 1.5, 1500)

# Draw graph;
fig, ax = plt.subplots(1)

violin = ax.violinplot([data_a, data_b, data_c], positions=[2, 3, 4])
ax.set_ylim(-10, 10)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

plt.show()


# Show means, medians, min/max;
fig, ax = plt.subplots(1)

# showmeans=False, showmedians=False, showextrema=True
violin = ax.violinplot([data_a, data_b, data_c], showmeans=True)
ax.set_ylim(-10, 10)
ax.set_xticks(np.arange(1, 4))
ax.set_xticklabels(["A", "B", "C"])
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

plt.show()

# Show IQR;
fig, ax = plt.subplots(1)

violin = ax.violinplot([data_a, data_b, data_c], quantiles=[[0.25, 0.75], [0.1, 0.9], [0.3, 0.7]])
ax.set_ylim(-10, 10)
ax.set_xticks(np.arange(1, 4))
ax.set_xticklabels(["A", "B", "C"])
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

plt.show()

# Color setting
fig, ax = plt.subplots(1)

violin = ax.violinplot([data_a, data_b, data_c], showmeans=True)
ax.set_ylim(-10, 10)
ax.set_xticks(np.arange(1, 4))
ax.set_xticklabels(["A", "B", "C"])
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

# Set color of bodies;
violin["bodies"][0].set_facecolor("blue")
violin["bodies"][1].set_facecolor("red")
violin["bodies"][2].set_facecolor("green")

# Color of vertical axis;
violin["cbars"].set_edgecolor("black")
# Color of the max point;
violin["cmaxes"].set_edgecolor("gray")
# Color of the min point;
violin["cmins"].set_edgecolor("red")
# Color of the mean point;l
violin["cmeans"].set_edgecolor("blue")

plt.show()