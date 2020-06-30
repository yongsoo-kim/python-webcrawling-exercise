import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path  # For file path check

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# [Speed] Tuple > List
# Because Tuple is immutable. Use this data type for constants or properties.

# ---------------
# Tuple type-
# ---------------
# Order -> O
# Duplicate -> O
# Modification -> X
# Delete -> X


# declaration
a = ()
b = (0,) #DON't miss comma for even 1 element. If you miss this, this will become 'int'.
c = (0, 1, 2, 3)
d = (0, 1, 'car', 'apple', 'apart')
e = (0, 1, ('car', 'apple', 'apart'))

# Indexing
print('#==========#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1])) # convert to list

# Slicing
print('#==========#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# Tuple calculation
print('#==========#')
print('c + d -', c + d)
print('c * 3 -', c * 3)
print("'hi' + c[0] -", 'hi' + str(c[0]))

# Tuple function
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))
