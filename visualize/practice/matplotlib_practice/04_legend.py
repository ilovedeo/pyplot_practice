import matplotlib.pyplot as plt

# https://wikidocs.net/137778

# Set legend by default setting;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label="Price ($)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

# Set location of legend manually (proportion_x, proportion_y);
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label="Price ($)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
# plt.legend(loc=(0.0, 0.0)) # Bottom left;
# plt.legend(loc=(0.5, 0.5)) # Center;
# plt.legend(loc=(1.0, 1.0)) # Top right;
plt.legend(loc=(0.77, 0.03)) # Bottom right;
plt.show()

# Set location by string;
plt.plot([1, 2, 3, 4], [1, 3, 5, 7], label="Price ($)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend(loc="lower right")
plt.show()

# Plot multiple;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label="Price ($)")
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label="Demand (#)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
# plt.legend(loc="best")
plt.legend(loc="best", ncol=2, fontsize=14)
plt.show()

# Legend frame setting;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label="Price ($)")
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label="Demand (#)")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
# plt.legend(loc="best")
plt.legend(loc="best", ncol=2, fontsize=14, frameon=False, shadow=True)
plt.show()
