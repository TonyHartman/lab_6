import pandas as pd
import matplotlib.pyplot as plt

'''Вывести DataFrame из 2 столбцов: число звонков в поддержку; доля оттока (Churn). Построить график.'''
f = pd.read_csv("telecom_churn.csv")
series1 = f.groupby(["Customer service calls"])["Customer service calls"].count()
series2 = f.groupby(["Customer service calls"]).agg({"Churn": "mean"})["Churn"]
df = pd.concat([series1, series2], axis=1)
print(df)
df.plot(x="Customer service calls", y="Churn", kind='bar')
plt.show()
