import pandas as pd
import numpy as np
'''
Добавьте к созданному датафрейму четвертый столбец, равный среднему значению первых трех, используя функцию mean.
'''

'''
df = pd.DataFrame({"A": [2, 3, 9], "B": [5, 6, 6]}, index=[1, 2, 3])
df["C"] = df["A"]**2 + df["B"]**2
df["D"] = df.mean(axis=1)
print(df)
'''

df1 = pd.DataFrame(np.random.randn(3, 2), columns=list('AB'))
df1["C"] = df1["A"]**2 + df1["B"]**2
df1["D"] = df1.mean(axis=1)
print(df1)