import pandas as pd
import numpy as np

'''
Создайте датафрейм из 2 столбцов, заполненных произвольными числами. Добавьте третий столбец, равный их сумме квадратов.
'''
#df = pd.DataFrame({"A": [2, 3, 9], "B": [5, 6, 6]}, index=[1, 2, 3])
#df["C"] = df["A"]**2 + df["B"]**2
#print(df)

df1 = pd.DataFrame(np.random.randn(3, 2), columns=list('AB'))
df1["C"] = df1["A"]**2 + df1["B"]**2
print(df1)