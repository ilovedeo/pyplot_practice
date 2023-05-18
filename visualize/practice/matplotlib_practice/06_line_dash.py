import matplotlib.pyplot as plt


# https://wikidocs.net/137791

###
# Set line style;
plt.plot([1, 2, 3], [4, 4, 4], "-", color="C0", label="solid")
plt.plot([1, 2, 3], [3, 3, 3], "--", color="C0", label="Dashed")
plt.plot([1, 2, 3], [2, 2, 2], ":", color="C0", label="Dotted")
plt.plot([1, 2, 3], [1, 1, 1], "-.", color="C0", label="Dash-dot")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.axis([0.8, 3.2, 0.5, 5.0])
plt.legend(loc="upper right", ncol=4)
plt.show()

###
# Use "linestyle" setting;
plt.plot([1, 2, 3], [4, 4, 4], linestyle="solid", color="C0", label="'solid'")
plt.plot([1, 2, 3], [3, 3, 3], linestyle="dashed", color="C0", label="'dashed")
plt.plot([1, 2, 3], [2, 2, 2], linestyle="dotted", color="C0", label="'dotted'")
plt.plot([1, 2, 3], [1, 1, 1], linestyle="dashdot", color="C0", label="'dashdot'")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.axis([0.8, 3.2, 0.5, 5.0])
plt.legend(loc="upper right", ncol=4)
plt.tight_layout()
plt.show()

###
# 선 끝 모양 지정;





