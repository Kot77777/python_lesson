import pandas as pd
from networkx import reverse

sp = input().split()
sp2 = []
for i in sp:
    sp2.append(sp.count(i))

data = {
    'count': sp2,
    'name': sp
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by=['count', 'name'], ascending=[False, True])
df_unique = df_sorted.drop_duplicates()

for index, row in df_unique.iterrows():
    print(f"{row['count']} {row['name']}")