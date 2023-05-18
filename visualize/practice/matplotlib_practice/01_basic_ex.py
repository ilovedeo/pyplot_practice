import matplotlib.pyplot as plt
import numpy as np

# https://wikidocs.net/92071

# First example;
# plt.plot(x, y)
# Same as plt.plot([0, 1, 2, 3], [1, 2, 3, 4])
plt.plot([1, 2, 3, 4])
plt.show()

# Second example;
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# Second example;
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
plt.axis([0, 6, 0, 20])
plt.show()

# Third example: plot multiple;
# plt.plot(Xvec, Y1vec, 'style', Xvec, Y2vec, 'r--, bs, g^, ...')
t = np.arange(0, 5, 0.2)
plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
plt.show()
