import matplotlib.pyplot as plt

###
# Add 1 subplot;
fig, ax = plt.subplots()
plt.show()

###
# Add 1 subplot 2;
# add_axes([left, bottom, width, height])
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
plt.show()

###
# Plot multiple plots;
fig, ax = plt.subplots(2, 2)
plt.show()

# Share x/y axis
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
plt.show()