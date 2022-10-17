import pandas as pd

'''
Какие звонки дольше - дневные, вечерние или ночные? Ответ привести в формате DataFrame  3∗3 :
строки - число минут, число звонков, среднее время звонка. Столбцы - день, вечер, ночь
 '''

f = pd.read_csv("telecom_churn.csv")
day_calls = f.groupby(["State"]).agg({"Total day calls": "sum"}).sum()[0]
day_min = f.groupby(["State"]).agg({"Total day minutes": "sum"}).sum()[0]
day_mean = day_min / day_calls
evening_calls = f.groupby(["State"]).agg({"Total eve calls": "sum"}).sum()[0]
evening_min = f.groupby(["State"]).agg({"Total eve minutes": "sum"}).sum()[0]
evening_mean = evening_calls / evening_min
night_calls = f.groupby(["State"]).agg({"Total night calls": "sum"}).sum()[0]
night_min = f.groupby(["State"]).agg({"Total night minutes": "sum"}).sum()[0]
night_mean = night_min / night_calls
df = pd.DataFrame({"Calls": [day_calls, evening_calls, night_calls], "Minutes": [day_min, evening_min, night_min], "Mean time": [day_mean, evening_mean, night_mean]}, index = ["Day", "Evening", "Night"])
print(df)