import numpy as np
import matplotlib.pyplot as plt

# ax.quiver(x_pos_vec, y_pos_vec, x_direction_vec, y_direction_vec, color)
# note: x_pos_vec.shape = y_pos_vec.shape = x_direction_vec.shape = y_direction_vec.shape

###
# Create single vector;
x_pos, y_pos = (0, 0)
x_dir, y_dir = (1, 1)

fig, ax = plt.subplots(figsize=(12, 7))
ax.quiver(x_pos, y_pos, x_dir, y_dir)
ax.set_title("Quiver plot with one arrow")

plt.show()

# Create 3 vectors;
x_pos = [0, 0, 0]
y_pos = [0, 0, 0]
x_dir = [1, 0, 1]
y_dir = [0, 1, 1]

fig, ax = plt.subplots(figsize=(12, 7))
ax.quiver(x_pos, y_pos, x_dir, y_dir, scale=5)
ax.axis([-1.5, 1.5, -1.5, 1.5])
plt.show()

###
# Create multiple vectors;
x = np.arange(0, 2.2, 0.2)
y = np.arange(0, 2.2, 0.2)

X, Y = np.meshgrid(x, y)
u = np.cos(X) * Y
v = np.sin(Y) * Y

# creating plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.quiver(X, Y, u, v)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([-0.3, 2.3, -0.3, 2.3])
ax.set_aspect("equal")

plt.show()

###
# Creating arrows;
x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)

# Creating gradient;
X, Y = np.meshgrid(x, y)
z = X * np.exp(-X**2 - Y**2)

dx, dy = np.gradient(z)

# Creating plot.
fig, ax = plt.subplots(figsize=(9, 9))
ax.quiver(X, Y, dx, dy)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect("equal")

plt.show()