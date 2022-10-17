import pandas as pd

'''
 Выведите датафрейм размера  3∗2 : столбцы State, Churn для 100, 102 и 104 строк исходного датафрейма.
'''

f = pd.read_csv("telecom_churn.csv")
fs0 = f.loc[100, "State"]
fs2 = f.loc[102, "State"]
fs4 = f.loc[104, "State"]

fc0 = f.loc[100, "Churn"]
fc2 = f.loc[102, "Churn"]
fc4 = f.loc[104, "Churn"]

df = pd.DataFrame({"State": [fs0, fs2, fs4], "Churn": [fc0, fc2, fc4]}, index = ["100", "102", "104"])
print(df)