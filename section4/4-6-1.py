import io
import sys
import pandas as pd
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Basic read1
df = pd.read_excel('excel_s1.xlsx', sheet_name=0)
print(df)
print(df.head())  # Show first 5 rows
print(df.tail())  # Show last 5 rows

# Row, footer skip
df = pd.read_excel('excel_s1.xlsx', skiprows=[0], skipfooter=10)  # Skip first row and last 10 rows.
print(df)

# Header redefinition(1)
df = pd.read_excel('excel_s1.xlsx', header=0)
print(df)
print(list(df))
print(list(df.columns.values))

# Header redefinition(2)
df = pd.read_excel('excel_s1.xlsx', skiprows=[0], header=None, names=['State', 2017, 2019, 2020])
print(df)

# Replace values
df = pd.read_excel('excel_s1.xlsx', header=0, na_values='...', converters={"2003": lambda w: w if w > 60000 else None})
print(df)
print(pd.isnull(df))

# Index redefinition
df = pd.read_excel('excel_s1.xlsx', header=0)
print(df)
print(df.rename(index=lambda x: x + 1))
print(df.rename(index=lambda x: x + 1).index)
