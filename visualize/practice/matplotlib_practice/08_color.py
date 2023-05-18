import matplotlib.pyplot as plt

###
# Use format string;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], "r")
plt.plot([1, 2, 3, 4], [2, 2.8, 4.3, 6.5], "g")
plt.plot([1, 2, 3, 4], [2, 2.5, 3.3, 4.5], "b")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

###
# Use "color" parameter
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], color="limegreen")
plt.plot([1, 2, 3, 4], [2, 2.8, 4.3, 6.5], color="violet")
plt.plot([1, 2, 3, 4], [2, 2.5, 3.3, 4.5], color="dodgerblue")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

###
# Use hex code;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], color="#e35f62", marker="o", linestyle="--")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

