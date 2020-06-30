import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path  # For file path check

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# ---------------
# Sets Type -> Good for using group(A and B 's intersection, union, difference)!
# ---------------
# Order -> X
# Duplicate -> X
# Modification -> O
# Delete -> O

# declaration
a = set()
b = set([1, 2, 3, 4])

print(type(b))
print(b)

# Set -> You can't indexing this! So you need to change this to tuple or list.
t = tuple(b)
print(type(t), t)
print(t[0:2])

l = list(b)
print(type(l), l)
print(l[0:2])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# Intersection
print('t - ', s1 & s2)
print('t - ', s1.intersection(s2))

# Union
print('t - ', s1 | s2)
print('t - ', s1.union(s2))

# Difference
print('t - ', s1 - s2)
print('t - ', s1.difference(s2))

# add & delete
s3 = set([0, 1, 2, 3])
s3.add(4)
print('s3 -', s3)

s3.remove(2)
print('s3 -', s3)
