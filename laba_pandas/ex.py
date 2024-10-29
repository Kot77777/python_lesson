import pandas as pd
import matplotlib.pyplot as plt
data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [42 * i  for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)

# Ещё можно при желании создавать новые колонки на лету
df.loc[1:2, 'F'] = 'test'
print(df)