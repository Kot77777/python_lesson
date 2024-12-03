import pandas as pd

N = int(input())
time_stamp = []
id = []
vit_d = []
acat = []
anti_tg = []
neural_activity = []
mch = []

sp = []
for i in range(N):
    sp = list(map(float, input().split()))
    time_stamp.append(sp[0])
    id.append(sp[1])
    vit_d.append(sp[2])
    acat.append(sp[3])
    anti_tg.append(sp[4])
    neural_activity.append(sp[5])
    mch.append(sp[6])
    sp.clear()

data = {
    'id': list(map(int, id)),
    'neural_activity': neural_activity
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by=['id'])

price = {int(row["id"]): [] for index, row in df_sorted.iterrows()}
for index, row in df_sorted.iterrows():
    price[row["id"]].append(row["neural_activity"])

total = {key: item for key, item in price.items() if len(item) > 1}
deff = {key: max(item) - min(item) for key, item in total.items()}

sorted_dict = sorted(deff.items(), key=lambda item: item[1], reverse=False)
silon = []
for i in range(len(sorted_dict)):
    if i > 2:
        break
    silon.append(sorted_dict[i][0])
print(*silon)

