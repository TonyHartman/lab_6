import pandas as pd

f = pd.read_csv("telecom_churn.csv")
m = f.groupby(["State"]).agg({"Total day calls": "mean"}).mean()[0]
print(m)