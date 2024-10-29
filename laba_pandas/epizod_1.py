import pandas as pd

df1 = pd.read_csv("transactions.csv", sep=',')

print('====================================================')

status_ok = df1[df1["STATUS"] == "OK"].sort_values(by='SUM', ascending=False)
print("3 самых крупных платежа из реально проведённых", status_ok.iloc[:, [1, 3]].head(3).to_string(index=False), sep='\n')

print('====================================================')

umbrella = status_ok.loc[status_ok["CONTRACTOR"] == "Umbrella, Inc", 'SUM']
print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc: ", umbrella.sum())
