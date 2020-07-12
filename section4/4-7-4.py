import io
import sys
import matplotlib.pyplot as plt

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# list range (x axis)
x = range(0, 256)
print(x)

# List range (Y axis)
y = []
for v in x:
    y.append(v * v)
print(y)

# Or, This will work too.
# y = [v * v for v in x]
# print(y)

#Chart settings
# plt.plot(x, y, 'b') # Blue color graph
# plt.plot(x, y, 'r') # Red color graph
# plt.plot(x, y, 'b--') # Dotted line graph
plt.plot(x, y, 'bo') # Bold line graph
# Run chart
plt.show()



