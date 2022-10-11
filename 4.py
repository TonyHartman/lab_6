import pandas as pd

f = pd.read_csv("telecom_churn.csv")
LA = f.groupby(["State"]).agg({"Total day calls": "mean"}).loc["LA"][0]
print(LA)