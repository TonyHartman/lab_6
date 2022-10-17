import pandas as pd

'''
Отсортриуйте штаты по Total day charge (по возрастанию).
'''

f = pd.read_csv("telecom_churn.csv")
series = f.groupby(["State"]).agg({"Total day charge": "mean"}).sort_values(by="Total day charge", ascending = True)
print(series)
