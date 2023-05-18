import matplotlib.pyplot as plt

# https://wikidocs.net/92083

###
# Set the color, and shape of the markers;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], "bo")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

###
# Set the color, shape and line of the markers
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], "bo-.")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

###
# Use "marker" parameter;
plt.plot([4, 5, 6], marker="H")
plt.plot([3, 4, 5], marker="d")
plt.plot([2, 3, 4], marker="x")
plt.plot([1, 2, 3], marker=11)
plt.plot([0, 1, 2], marker="$Z$")
plt.show()
