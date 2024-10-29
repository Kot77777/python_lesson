import pandas as pd

w1 = input()
w2 = input()

df1 = pd.read_csv(w1, sep=';')
df2 = pd.read_csv(w2, sep=';')

merged_df = df1.merge(df2, on='id')

mean_scores = merged_df.groupby(['name', 'company'])['mark'].mean().reset_index()
mean_scores['mean'] = mean_scores['mark'].round(3)

top_games = mean_scores.sort_values(by='mean', ascending=False).head(3)
for index, row in top_games.iterrows():
    print(f"{row['name']} {row['mean']:.3f}")

high_rated_games = mean_scores[mean_scores['mean'] > 8.0]
studio_counts = high_rated_games['company'].value_counts().head(1)

best_studio = studio_counts.idxmax()
best_count = studio_counts.max()
print(f"{best_studio} {best_count}")
