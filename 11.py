import pandas as pd

f = pd.read_csv("telecom_churn.csv")

'''Вывести DataFrame из 2 столбцов: число звонков в поддержку;
 число клиентов, звонивших столько раз. Подсказка: используйте функцию агрегации count.'''

df = f.groupby(["Customer service calls"])["Customer service calls"].count()
print(df)