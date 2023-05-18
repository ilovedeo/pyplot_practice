import matplotlib.pyplot as plt

# https://wikidocs.net/92082

# Set x, y limit manually;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.xlim([0, 5])
plt.ylim([0, 20])
plt.show()

# Use axis option: string input;
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.axis("equal")
plt.show()

# Check limit;
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)

axis_range = plt.axis()
print(axis_range)

plt.show()



