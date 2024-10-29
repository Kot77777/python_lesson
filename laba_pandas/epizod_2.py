import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("flights.csv", sep=',')

print('====================================================')

price = {row["CARGO"]: 0 for index, row in df1.iterrows()}
for index, row in df1.iterrows():
    price[row["CARGO"]] += row["PRICE"]
print("Полная стоимость для каждой авиакомпании: ", price)

print('====================================================')

weight = {row["CARGO"]: 0 for index, row in df1.iterrows()}
for index, row in df1.iterrows():
    weight[row["CARGO"]] += row["WEIGHT"]
print("Полная масса груза для каждой авиакомпании: ", weight)

print('====================================================')

reis = {row["CARGO"]: df1["CARGO"].value_counts().get(row["CARGO"], 0) for index, row in df1.iterrows()}
print("Количество рейсов для каждой авиакомпании: ", reis)

fig, ax = plt.subplots(1, 3, figsize=(15, 8))
keys = list(price.keys())
values = list(price.values())
ax[0].bar(keys, values)
ax[0].set_title('Полная стоимость для каждой авиакомпании')
ax[0].set_xlabel('Название авиакомпании')
ax[0].set_ylabel('Значения стоимости')

keys1 = list(weight.keys())
values1 = list(weight.values())
ax[1].bar(keys1, values1)
ax[1].set_title('Полная масса груза для каждой авиакомпании')
ax[1].set_xlabel('Название авиакомпании')
ax[1].set_ylabel('Значения массы')

keys2 = list(reis.keys())
values2 = list(reis.values())
ax[2].bar(keys2, values2)
ax[2].set_title('Количество рейсов для каждой авиакомпании')
ax[2].set_xlabel('Название авиакомпании')
ax[2].set_ylabel('Количество рейсов')

plt.subplots_adjust(wspace=0.4)
plt.savefig('Epizod_2.png', dpi=300)
plt.show()