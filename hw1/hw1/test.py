import pandas as pd
import numpy as np

s = pd.Series([1,3,5,7,9])
print(s)
index = np.array(['A','B','C','D','E','F'])
column = np.array(['a','b','c','d'])
df = pd.DataFrame(np.random.rand(6,4), index=index, columns=column)
print(df)