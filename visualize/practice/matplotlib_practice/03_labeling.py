import matplotlib.pyplot as plt

# https://wikidocs.net/92081

# Basic labeling;
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("X-Lable")
plt.ylabel("Y-Label")
plt.show()

# Set space from each axis;
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("X-Axis", labelpad=15)
plt.ylabel("Y-Axis", labelpad=20)
plt.show()

# Font setting;
font_x = {
    "family": "serif",
    "color": "b",
    "weight": "bold",
    "size": "14"
}

font_y = {
    "family": "fantasy",
    "color": "deeppink",
    "weight": "normal",
    "size": "xx-large"
}

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel("X-Axis", labelpad=10, fontdict=font_x)
plt.ylabel("Y-Axis", labelpad=10, fontdict=font_y)
plt.show()

# Set label's location;
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel("X-Axis", loc="right")
plt.ylabel("Y-Axis", loc="top")
plt.show()