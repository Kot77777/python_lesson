import pandas as pd

w1 = input()
w2 = input()

df1 = pd.read_csv(w1, sep=';')
df2 = pd.read_csv(w2, sep=';')

citation_count = {row['title']: 0 for index, row in df1.iterrows()}

for index, row in df2.iterrows():
    if row['reference'] in citation_count:
        citation_count[row['reference']] += 1

author_cit = {row['author']: 0 for index, row in df1.iterrows()}

author_num_of_st = {row['author']: (df1['author'].value_counts().get(row['author'], 0)) for index, row in df1.iterrows()}

for index, row in df1.iterrows():
    author_cit[row['author']] += citation_count[row['title']]

author_sr = {row['author']: (author_cit[row['author']] / author_num_of_st[row['author']]) for index, row in df1.iterrows()}

author_sr_sort = dict(sorted(author_sr.items(), key=lambda item: item[1], reverse=True))

for index, (key, value) in enumerate(author_sr_sort.items()):
    if index < 3:
        print(f'{key} {value:.3f}')