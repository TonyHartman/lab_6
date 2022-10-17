import pandas as pd

'''
Сделайте агрегацию по средним показателям для каждой Area code.
'''

f = pd.read_csv("telecom_churn.csv")
series = f.groupby("Area code").mean()
print(series)