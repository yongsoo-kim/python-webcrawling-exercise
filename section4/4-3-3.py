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
# Dictionary Type
# ---------------
# Order -> X
# Duplicate -> X
# Modification -> O
# Delete -> O

# declaration
a = {'name': 'kim', 'phone': '2357864', 'birth': 19651209}
b = {0: 'Hello World!'}  # 'int' type can be key(not common)
c = {'arr': [0, 1, 2, 3]}
print(type(a), a)

# Output
print('a - ', a['name'])
print('a - ', a.get('name'))
print('a - ', a.get('unknown'))  # This won't be error. Value will be None.
print('c - ', c.get('arr'))
print('c - ', type(c.get('arr')))

# Add
a['address'] = 'Seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

print('a -', list(a.keys()))  # You can now use this for loop.
print('a - ', a.values())
print('a - ', a.items())  # Return (key, value) tuple.
print('a - ', type(list(a.items())[1]))

print('a - ', 'name' in a)  # key existence check.
print('a - ', 'unknown' in a)

