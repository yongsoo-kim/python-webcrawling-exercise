import io
import sys
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Basic read
df = pd.read_csv('csv_s1.csv')
print(df)

# Skip rows
df = pd.read_csv('csv_s1.csv', skiprows=[0, 1])
print(df)

# Skip rows, omit headers
df = pd.read_csv('csv_s1.csv', skiprows=[0], header=None)
print(df)

# Header define
df = pd.read_csv('csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014,
                                                                 2015])  # Skip row -> Remove original header. # header=None -> Prevent first header from becoming header # Names -> real header!
print(df)

# Index column define
df = pd.read_csv('csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015], index_col=[0])
print(df)

# We will check this when we study excel....
df = pd.read_csv('csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015], index_col=[0],
                 na_values=['JAN'])
print(df)
print(pd.isnull(df))

# Index column define
df = pd.read_csv('csv_s1.csv', skiprows=[0], header=None, names=["Month", 2013, 2014, 2015])
print(df.index)
print(list(df.index))
print(df.index.values)
print(df.index.values.tolist())
# print(df.rename(index={0:'aa',1:'bb',0:'cc',})) # Using dictonary is too troublesome and long... Use Lambda.
# print(df.rename(index=lambda x:x*10))


# ----------------------------------
# Read
df2 = pd.read_csv('csv_s2.csv', sep=';')
print(df2)

# Change Column values
df2 = pd.read_csv('csv_s2.csv', sep=';', skiprows=[0], header=None,
                  names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
print(df2['Grade']) # Print only Grade column
df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
print(df2)

#Add Average column
df2 = pd.read_csv('csv_s2.csv', sep=';', skiprows=[0], header=None,
                  names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) # axis=0 -> Vertical axis=1-> Horizontal
print(df2)

#Add Sum column
df2 = pd.read_csv('csv_s2.csv', sep=';', skiprows=[0], header=None,
                  names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1) # axis=0 -> Vertical axis=1-> Horizontal
print(df2)


