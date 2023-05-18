import matplotlib.pyplot as plt
import numpy as np

plt.style.use("default")
plt.rcParams["figure.figsize"] = (4.5, 3)
plt.rcParams["font.size"] = 5

x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.plot(x, y1, color="green")

ax2 = ax1.twinx()
ax2.plot(x, y2, color="deeppink")

plt.show()

###
# Different label setting;
x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Axis")
ax1.set_ylabel("1st Y-Axis")
ax1.plot(x, y1, color="green")

ax2 = ax1.twinx()
ax2.set_ylabel("2nd Y-Axis")
ax2.plot(x, y2, color="deeppink")

plt.show()

###
# Legend setting;
x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Axis")
ax1.set_ylabel("1st Y-Axis")
ax1.plot(x, y1, color="green", label="1st Data")
ax1.legend(loc="upper right")

ax2 = ax1.twinx()
ax2.set_ylabel("2nd Y-Axis")
ax2.plot(x, y2, color="deeppink", label="2nd Data")
ax2.legend(loc="lower right")

plt.show()

###
# Merge legend information;
x = np.arange(0, 3)
y1 = x + 1
y2 = -x - 1

fig, ax1 = plt.subplots()

ax1.set_xlabel("X-Axis")
ax1.set_ylabel("1st Y-Axis")
# line_1: list with "matplotlib.lines.Line2D object";
line_1 = ax1.plot(x, y1, linestyle="--", label="1st Data")

ax2 = ax1.twinx()
ax2.set_ylabel("2nd Y-Axis")
# line_2: list with "matplotlib.lines.Line2D object";
line_2 = ax2.plot(x, y2, linestyle=":", label="2nd Data")

lines = line_1 + line_2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper right")

plt.show()
