import pandas as pd

f = pd.read_csv("telecom_churn.csv")
m = f.groupby(["State"]).agg({"Total day calls": "mean"}).mean()[0]
new_dataframe = f.groupby(["State"]).agg({"Total day calls": "mean", "Total eve calls": "mean"})
print(new_dataframe)