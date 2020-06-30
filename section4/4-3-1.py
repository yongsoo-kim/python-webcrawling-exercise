import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path  # For file path check

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

a = 'hello'
print(type(a))
print(a[0])
print(a[0:3])
print(a[-1])

for t in a:
    print(t, type(t))

# ---------------
# List type
# ---------------
# Order -> O
# Duplicate -> O
# Modification -> O
# Delete -> O

# declaration
a = []
b = list()
c = [0, 0, 1, 2]
d = [0, 1, 'car', 'apple', 'apart']
e = [0, 1, ['car', 'apple', 'apart']]

# Indexing
print("#=======#")
print('d - ', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])  # calculation ok
print('d -', e[-1][1])
print('d -', e[2][1])

# Slicing
print("#=======#")
print('d - ', d[0:3])
print('d - ', d[2:])

# Calculation
print("#=======#")
print('c + d', c + d)
print('c * 3 ', c * 3)
print('hi + c[0]', 'hi' + str(c[0]))

# List update, delete
print("#=======#")
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c -', c)
c[1:3] = []  # Delete many elements
print('c -', c)
del c[3]
print('c - ', c)

# List function
print("#=======#")
a = [5, 2, 3, 1, 4]
print('a -', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(4), a[4])  # These 2 ways are the same.
print('a - ', a.count(1))
a.remove(2)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)

ex = [8, 9]
a.extend(ex)
print('a - ', a)

# For list remove -> del, remove, pop
while a:
    l = a.pop()
    print(l is 4)
