import pandas as pd

f = pd.read_csv("telecom_churn.csv")
TotalDayCalls = f.groupby(["State"]).agg({"Total day calls": "mean"})
print(TotalDayCalls)