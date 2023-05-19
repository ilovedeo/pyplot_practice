import matplotlib.pyplot as plt
import numpy as np

# Setting basic style;
plt.style.use("default")
plt.rcParams["figure.figsize"] = (4.5, 3)
plt.rcParams["font.size"] = 7

# Data import;
np.random.seed(0)
data_a = np.random.normal(0, 2.0, 1000)
data_b = np.random.normal(-3, 1.5, 500)
data_c = np.random.normal(1.2, 1.5, 1500)

# Draw figure, whisker range: Q3 + whis * (Q3-Q1);
fig, ax = plt.subplots(1)

ax.boxplot([data_a, data_b, data_c], whis=1.5)
ax.set_ylim(-10, 10)
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

plt.show()

# Add notch.
fig, ax = plt.subplots(1)

# Longer whiskers.
ax.boxplot([data_a, data_b, data_c], notch=True, whis=2.5)
ax.set_ylim(-10, 10)
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

plt.show()

# Get whisker data;
fig, ax = plt.subplots(1)

box = ax.boxplot([data_a, data_b, data_c], notch=True, whis=1.5)
ax.set_ylim(-10, 10)
ax.set_xlabel("Data Type")
ax.set_ylabel("Value")

# box: whiskers, caps, boxes, medians, fliers, means;
# arr[min, Q1], arr[Q3, max]
whiskers = [item.get_ydata() for item in box["whiskers"]]
medians = [item.get_ydata() for item in box["medians"]]
# values outside whiskers;
fliers = [item.get_ydata() for item in box["fliers"]]

print("whiskers: \n", whiskers)
print("medians: \n", medians)
print("fliers: \n", fliers)

plt.show()

# Vertical boxplot;
fig, ax = plt.subplots(1)

ax.boxplot([data_a, data_b, data_c], notch=True, whis=1.5, vert=False)
ax.set_xlim(-10, 10)
ax.set_xlabel("value")
ax.set_ylabel("Data Type")

plt.show()

