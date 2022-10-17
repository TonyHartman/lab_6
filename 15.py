import pandas as pd

'''
Сравнить Total day charge для оставшихся и ушедших клиентов.
'''

f = pd.read_csv("telecom_churn.csv")

left = f[f["Churn"] == False].groupby(["State"]).agg({"Total day charge": "sum"}).sum()[0]
went = f[f["Churn"] == True].groupby(["State"]).agg({"Total day charge": "sum"}).sum()[0]
if left > went:
    print("Total day charge of left clients is bigger")
if left == went:
    print("Total day charge is equal")
if left < went:
    print("Total day charge of left clients is smaller")
