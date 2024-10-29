import matplotlib.pyplot as plt
import pandas as pd

stud_inf = pd.read_excel("students_info.xlsx")
result = pd.read_html("results_ejudge.html")[0]

sp_group_facult = []
for index, row in result.iterrows():
    matches = stud_inf.loc[stud_inf["login"] == row["User"]]

    if not matches.empty:
        ind = matches.index
        sp_group_facult.append(stud_inf.loc[ind, "group_faculty"])

result.loc[0:len(sp_group_facult)-1, 'group_faculty'] = sp_group_facult

sp_group_inform = []
for index, row in result.iterrows():
    matches = stud_inf.loc[stud_inf["login"] == row["User"]]

    if not matches.empty:
        ind = matches.index
        sp_group_inform.append(stud_inf.loc[ind, "group_out"])

result.loc[0:len(sp_group_inform)-1, 'group_out'] = sp_group_inform
result_full = result.fillna(0)

facult = {str(int(row["group_out"])): result_full.loc[result_full["group_out"] == row["group_out"], 'Solved'].mean().round(3) for index, row in result_full.iterrows() if int(row["group_out"])!=0}
inform = {str(int(row["group_faculty"])): result_full.loc[result_full["group_faculty"] == row["group_faculty"], 'Solved'].mean().round(3) for index, row in result_full.iterrows() if int(row["group_faculty"])!=0}

User = result_full.loc[(result_full["G"] >= 10.0) | (result_full["H"] >= 10.0), ['User', 'group_out', 'group_faculty']]

print('==========================================================================================')
print("Студенты, которые смогли пройти более одного теста в хотя бы одной из двух последних задач")
print('==========================================================================================')
for index, row in User.iterrows():
    print("User: ", row["User"], "пришел из факульт. группы ", int(row["group_out"]), "в группу по информ. ", int(row["group_faculty"]))

fig, ax = plt.subplots(1, 2, figsize=(15, 8))
keys = list(facult.keys())
values = list(facult.values())
ax[0].bar(keys, values)
ax[0].set_title('Среднее количество решённых задач по факультетским группам')
ax[0].set_xlabel('Факультетская группа')
ax[0].set_ylabel('Средний количество решённых задач')

keys1 = list(inform.keys())
values1 = list(inform.values())
ax[1].bar(keys1, values1)
ax[1].set_title('Среднее количество решённых задач по группам по информатике')
ax[1].set_xlabel('Группа по информатике')
ax[1].set_ylabel('Средний количество решённых задач')

plt.savefig('Epizod_3.png', dpi=300)
plt.show()
