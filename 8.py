import pandas as pd

f = pd.read_csv("telecom_churn.csv")
m = f.groupby(["State"]).agg({"Total day calls": "mean"}).mean()[0]
new_dataframe = f.groupby(["State"]).agg({"Total day calls": "mean", "Total eve calls": "mean"})
new_dataframe["There're more day calls"] = new_dataframe["Total day calls"] >= new_dataframe["Total eve calls"]
print(new_dataframe)