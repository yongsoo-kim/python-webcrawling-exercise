import io
import sys

from pandas import DataFrame

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

r_data = {'City': ['서울', '대구', '부산', '대전'], 'total1': [55000, 49000, 52000, 50000],
          'Total2': [65000, 59000, 62000, 60000]}
i_data = ['one', 'two', 'three', 'four']

# Print
print(type(r_data))
print(r_data)
print(type(i_data))
print(i_data)

# Define DataFrame
d_frame = DataFrame(r_data, index=i_data)
print(type(d_frame))
print(d_frame)
print(d_frame.index)
print(d_frame.values)
print(d_frame['City'])  # Columns
# print(d_frame.ix['one']) # .ix has been deprecated.
print(d_frame.loc['one'])
print(type(d_frame.loc['one']))  # n * Series = 1 * DataFrame

# Values loop
for e in d_frame.values:
    for i, z in enumerate(e):
        print(i, z)
