import pandas as pd

def yesNo(x):
    if x == "Yes":
        return(1)
    else:
        return(0)

f = pd.read_csv("telecom_churn.csv")
clients = f.shape[0]

df = pd.DataFrame({"international_plan": f["International plan"].apply(lambda x: yesNo(x)), "mail_plan": f["Voice mail plan"].apply(lambda x:yesNo(x))})

print(df["international_plan"].sum()/clients, df["mail_plan"].sum()/clients)