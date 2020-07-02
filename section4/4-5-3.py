import io
import sys
import pandas as pd
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Make random DataFrame
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=['ONE', 'TWO', 'THREE', 'FOUR'])
print(df)

df = pd.DataFrame(np.random.randn(100,4), columns=['ONE', 'TWO', 'THREE', 'FOUR'])
print(df)

#df.to_csv('result_s2.csv', index=False)
df.to_csv('result_s2.csv', index=False, header=False)