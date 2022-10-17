import pandas as pd

f = pd.read_csv("telecom_churn.csv")
intl = f.groupby(["State"]).agg({"Total intl minutes": "mean"}).mean()[0]
print(intl)