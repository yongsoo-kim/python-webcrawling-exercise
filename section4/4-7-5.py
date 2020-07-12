import io
import sys
import matplotlib.pyplot as plt

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# create 'fig' object
fig = plt.figure()

# Make sub slots(2 rows 1 column)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

x = range(0, 100)
# Create x axis
y = [v * v for v in x]

# Create y axis
z = [v * v * 2 for v in x]

# Line chart 1 row 1 colum
ax1.plot(x, y, 'b--', z, 'ro')

# Bar chart 2 rows 1 column
ax2.bar(x, z)

plt.show()
