import io
import sys
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Basic
df = pd.read_excel('excel_s1.xlsx', sheet_name=0)
print(df)

# Edit column value
print(df['State'].str)
df['State'] = df['State'].str.replace(' ', '|')
print(df)

# Add average column
df['Avg'] = df[['2003', '2004', '2005']].mean(axis=1).round(2)
print(df)

# Max value
# df['Max'] = df[['2003', '2004', '2005']].max(axis=0) #Max is in horizontal value! axis=0
print(df[['2003', '2004', '2005']].max(axis=0))

# Min value
print(df[['2003', '2004', '2005']].min(axis=0))

# Print detail into
print(df.describe())

# Write Excel file
df.to_excel('result_s1.xlsx', index=None)
